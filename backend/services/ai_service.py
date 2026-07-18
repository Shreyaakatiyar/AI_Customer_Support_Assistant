import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from prompts.support_prompt import support_prompt
from prompts.support_prompt import support_prompt, parser
from services.knowledge_service import load_knowledge

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    google_api_key = api_key
)

knowledge = load_knowledge()

chain = support_prompt | llm | parser

def generate_response(question: str):

    return chain.invoke(
        {
            "question": question,
            "knowledge": knowledge
        }
    )