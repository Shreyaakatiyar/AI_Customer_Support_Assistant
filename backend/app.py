from flask import Flask, jsonify, request
from services.ai_service import generate_response


app = Flask(__name__)


@app.route("/")
def home(): 
    return jsonify({
        "message" : "AI Customer Support Backend is running"
    })

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    
    question = data.get("question")

    if not question :
        return jsonify({
            "error" : "Question is required"
        }), 400

    response = generate_response(question)

    return jsonify({
        "response" : response
    })

if __name__ == "__main__" :
    app.run(debug=True)