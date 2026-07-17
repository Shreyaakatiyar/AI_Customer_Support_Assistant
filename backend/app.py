from flask import Flask, jsonify
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import os

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
    response = llm.invoke(
        "Explain Artificial Intelligence in one sentence."
    )

    return jsonify({
        "response" : response.content
    })

if __name__ == "__main__" :
    app.run(debug=True)