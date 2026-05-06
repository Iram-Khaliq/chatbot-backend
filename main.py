import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from database import SessionLocal, Message

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str
    conversation_id: str

@app.get("/")
def home():
    return {"message": "Server is running"}

@app.post("/chat")
def chat(req: ChatRequest):
    db = SessionLocal()

    try:
        messages = db.query(Message).filter(
            Message.conversation_id == req.conversation_id
        ).order_by(Message.id).all()

        chat_history = [
            {"role": "system", "content": "You are a helpful assistant."}
        ]

        chat_history += [
            {"role": m.role, "content": m.content}
            for m in messages
        ]

        chat_history.append({"role": "user", "content": req.message})

        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=chat_history
            )
            reply = response.choices[0].message.content
        except Exception as e:
            reply = f"Error: {str(e)}"

        db.add(Message(conversation_id=req.conversation_id, role="user", content=req.message))
        db.add(Message(conversation_id=req.conversation_id, role="assistant", content=reply))
        db.commit()

        return {"reply": reply}

    finally:
        db.close()
@app.get("/history/{conversation_id}")
def get_history(conversation_id: str):
    db = SessionLocal()

    try:
        messages = db.query(Message).filter(
            Message.conversation_id == conversation_id
        ).all()

        return [
            {"role": m.role, "content": m.content}
            for m in messages
        ]

    finally:
        db.close()