import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from prompts.support_prompt import support_prompt

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    google_api_key = api_key
)

def generate_response(question: str):

    prompt = support_prompt.invoke(
        {
            "question": question
        }
    )

    response = llm.invoke(prompt)

    return response.content