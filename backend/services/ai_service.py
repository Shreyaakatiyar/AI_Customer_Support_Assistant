import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from prompts.support_prompt import support_prompt, parser
from services.vector_service import retrieve_documents

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    google_api_key=api_key,
)

chain = support_prompt | llm | parser


def generate_response(question: str):
    """
    Generate an AI response using RAG.
    """

    documents = retrieve_documents(question)

    knowledge = "\n\n".join(
        doc.page_content for doc in documents
    )
    
    response = chain.invoke(
        {
            "question": question,
            "knowledge": knowledge,
        }
    )

    return response