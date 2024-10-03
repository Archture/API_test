from fastapi import FastAPI, Request, Header
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

# Define the model with an additional 'model' field
class Message(BaseModel):
    message: str
    model: str  # New 'model' field to be sent in the JSON body

@app.post("/message")
async def receive_message(msg: Message, token: str = Header(None)):
    # Log the message and model received
    print(f"Received message: {msg.message}")
    print(f"Received model: {msg.model}")

    # Extract the additional token from the headers
    print(f"Received token: {token}")

    # For the sake of this example, the response will return the message and model
    response_content = {"message": msg.message, "model": {token}}
    print(f"Sent response: {response_content}")

    return response_content

@app.get("/")
async def root():
    return {"message": "API is running"}
