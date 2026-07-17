import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from flask import Flask, jsonify
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from prompts.support_prompt import support_prompt

app = Flask(__name__)

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    google_api_key = api_key
)


@app.route("/")
def home(): 
    return jsonify({
        "message" : "AI Customer Support Backend is running"
    })

@app.route('/ask')
def ask():
    prompt =support_prompt.invoke(
        {
            "question" : "Explain Artificial Intelligence in one sentence."
        }
    )

    response = llm.invoke(prompt)

    return jsonify({
        "response" : response.content
    })

if __name__ == "__main__" :
    app.run(debug=True)