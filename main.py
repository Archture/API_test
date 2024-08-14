from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    message: str

@app.post("/message")
async def receive_message(msg: Message):
    # Log the message received
    print(f"Received message: {msg.message}")
    return {"reply": f"Message received: {msg.message}"}

@app.get("/")
async def root():
    return {"message": "API is running"}
