# AI Customer Support Assistant

An AI-powered Customer Support Assistant built using **Flask**, **LangChain**, **Google Gemini**, and **FAISS**. The assistant answers customer queries using Retrieval-Augmented Generation (RAG) by retrieving relevant information from a knowledge base before generating accurate and context-aware responses.

## Features

- AI-powered customer support chatbot
- Retrieval-Augmented Generation (RAG)
- LangChain Prompt Templates
- Google Gemini integration
- FAISS Vector Database for semantic search
- Structured JSON responses using Pydantic
- React-based chat interface
- Flask REST API
- Knowledge base built from text documents

---

## Tech Stack

### Frontend
- React (Vite)
- Axios
- CSS

### Backend
- Flask
- LangChain
- Google Gemini API
- FAISS
- Pydantic
- Python

---

## Project Structure

```
AI_Customer_Support_Assistant/
│
├── backend/
│   ├── app.py
│   ├── services/
│   ├── prompts/
│   ├── models/
│   ├── knowledge/
│   │   └── documents/
│   ├── vectorstore/
│   └── .env
│
├── frontend/
│   ├── src/
│   ├── components/
│   ├── services/
│   └── package.json
│
└── README.md
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Shreyaakatiyar/AI_Customer_Support_Assistant.git

cd AI_Customer_Support_Assistant
```

---

## Backend Setup

Navigate to the backend folder.

```bash
cd backend
```

Create a virtual environment.

```bash
python -m venv venv
```

Activate the virtual environment.

### Windows

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file inside the backend directory.

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

---

## Run the Backend

```bash
python app.py
```

Backend will run on:

```
http://127.0.0.1:5000
```

---

## Frontend Setup

Open another terminal.

```bash
cd frontend
```

Install dependencies.

```bash
npm install
```

Run the React application.

```bash
npm run dev
```

Frontend will run on:

```
http://localhost:5173
```

---

## API Endpoint

### POST `/chat`

#### Request

```json
{
  "question": "How long does shipping take?"
}
```

#### Response

```json
{
  "answer": "Standard shipping takes 3–5 business days, while express shipping takes 1–2 business days.",
  "category": "Shipping",
  "confidence": 100,
  "needs_human": false
}
```

---

## Knowledge Base

The chatbot retrieves information from text documents stored in:

```
backend/knowledge/documents/
```

Example documents:

- shipping.txt
- refund.txt
- billing.txt
- faq.txt

These documents are converted into vector embeddings and stored in a FAISS vector database for semantic retrieval.

---

## Workflow

```
User Question
      │
      ▼
React Frontend
      │
      ▼
Flask API
      │
      ▼
FAISS Retriever
      │
      ▼
Relevant Knowledge
      │
      ▼
Prompt Template
      │
      ▼
Google Gemini
      │
      ▼
Structured JSON Response
      │
      ▼
Frontend Chat Interface
```

---

## Sample Questions

- How long does shipping take?
- What is your refund policy?
- Can I cancel my order?
- Do you offer international shipping?
- How can I contact customer support?
- What payment methods are accepted?

---

## Future Improvements

- Conversation memory
- Source document citations
- Streaming AI responses
- Multi-user support
- Authentication
- Docker deployment
- Admin dashboard
- Support for PDF knowledge bases

---

## Author

**Shreyaa Katiyar**

GitHub: https://github.com/shreyaakatiyar