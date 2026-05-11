# AI Chatbot Backend

A FastAPI-based AI chatbot backend integrated with OpenAI API, SQLite database, and conversation memory support.

## Features

- FastAPI backend
- OpenAI GPT integration
- Conversation memory
- SQLite database storage
- Multiple conversation support
- REST API endpoints
- CORS enabled for React frontend integration

---

## Tech Stack

- Python
- FastAPI
- OpenAI API
- SQLite
- SQLAlchemy
- Uvicorn
- Python Dotenv

---

## Project Structure

```bash
poc1-chatbot/
│
├── main.py
├── database.py
├── chat.db
├── requirements.txt
├── .env
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/Iram-Khaliq/chatbot-backend.git
cd chatbot-backend
```

---

### Create Virtual Environment

```bash
python -m venv .venv
```

---

### Activate Virtual Environment

#### Windows

```bash
.\.venv\Scripts\activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the root folder:

```env
OPENAI_API_KEY=
```

---

## Run Server

```bash
python -m uvicorn main:app --reload
```

Server runs on:

```bash
http://127.0.0.1:8000
```

---

## API Endpoints

### Home Endpoint

```http
GET /
```

Response:

```json
{
  "message": "Server is running"
}
```

---

### Chat Endpoint

```http
POST /chat
```

Request Body:

```json
{
  "message": "Hello",
  "conversation_id": "user1"
}
```

Response:

```json
{
  "reply": "Hello! How can I help you?"
}
```

---

### Chat History Endpoint

```http
GET /history/{conversation_id}
```

Example:

```http
GET /history/user1
```

---

## Frontend Integration

This backend is designed to work with a React frontend application.

Frontend sends requests using:

```javascript
fetch("http://127.0.0.1:8000/chat")
```

---

## Deployment

Recommended platforms:

- Backend: Railway
- Frontend: Vercel

---

## Future Improvements

- User authentication
- Streaming responses
- Voice assistant integration
- File upload support
- Vector database memory
- Docker deployment

---

## Author

Developed by Iram
