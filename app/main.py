from fastapi import FastAPI
from pydantic import BaseModel
from chatbot import ChatBot


app = FastAPI()
bot = ChatBot()

class InputData(BaseModel):
    question: str
    language: str
    session_id: str

class RequestBody(BaseModel):
    input: InputData

@app.get("/")
async def root():
    print("Hello Roaming")
    return {"message": "Hello Roaming"}

@app.post("/chat")
async def chat(request: RequestBody):
    response = bot.get_response(request.input.session_id, request.input.question, request.input.language)
    return {"output": response}