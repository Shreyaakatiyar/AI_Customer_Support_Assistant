from pathlib import Path

from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS

import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

BASE_DIR = Path(__file__).resolve().parent.parent

DOCUMENTS_PATH = BASE_DIR / "knowledge" / "documents"
VECTOR_DB_PATH = BASE_DIR / "vectorstore"

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    google_api_key=api_key
)

INDEX_FILE = VECTOR_DB_PATH / "index.faiss"

if INDEX_FILE.exists():
    # Load existing index from disk
    vectorstore = FAISS.load_local(
        VECTOR_DB_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )
else:
    # Build index from documents, then save it
    loader = DirectoryLoader(
        DOCUMENTS_PATH,
        glob="*.txt",
        loader_cls=TextLoader
    )
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    chunks = text_splitter.split_documents(documents)

    vectorstore = FAISS.from_documents(chunks, embeddings)

    VECTOR_DB_PATH.mkdir(parents=True, exist_ok=True)
    vectorstore.save_local(VECTOR_DB_PATH)

retriever = vectorstore.as_retriever(search_kwargs={"k": 3})


def retrieve_documents(question: str):
    return retriever.invoke(question)