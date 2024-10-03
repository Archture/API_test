from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins. For more security, specify the origins you need.
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)


class Message(BaseModel):
    message: str

@app.post("/message")
async def receive_message(msg: Message):
    # Log the message received
    print(f"Received message: {msg.message}")
    response_content = msg.message
    print(f"Sent message: {response_content}")
    return response_content


@app.get("/")
async def root():
    return {"message": "API is running"}
