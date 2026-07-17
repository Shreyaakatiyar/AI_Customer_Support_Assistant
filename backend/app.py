from flask import Flask, jsonify
from dotenv import load_dotenv
from google import genai
import os

app = Flask(__name__)

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=api_key)


@app.route("/")
def home(): 
    return jsonify({
        "message" : "AI Customer Support Backend is running"
    })

@app.route('/ask')
def ask():
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents="Explain Artificial Intelligence in one sentence"
    )

    return jsonify({
        "response" : response.text
    })

if __name__ == "__main__" :
    app.run(debug=True)