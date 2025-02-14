import os
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from langchain_together import ChatTogether
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, FileResponse
from typing import List

# Load environment variables
load_dotenv()
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")

# Validate API Key
if not TOGETHER_API_KEY:
    raise ValueError("Missing TOGETHER_API_KEY in .env file")

# Initialize chatbot
llm = ChatTogether(
    model="meta-llama/Llama-3-70b-chat-hf",
    temperature=0.7,
    max_tokens=200,
    timeout=30,
    max_retries=2,
)

# Create FastAPI app
app = FastAPI()

# Enable CORS (for frontend communication)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
)

# Serve frontend files (index.html, styles.css, app.js)
app.mount("/static", StaticFiles(directory="frontend"), name="static")

# Serve the Chat UI (default homepage)
@app.get("/", response_class=FileResponse)
async def serve_ui():
    return "frontend/index.html"

# API status check
@app.get("/status/")
async def status():
    return JSONResponse(content={"status": "running", "model": "Llama-3-70b-chat-hf"})

# Data model for chatbot request
class ChatRequest(BaseModel):
    message: str


class ChatRequest(BaseModel):
    messages: List[dict]  # Expecting a list of messages
    
# Chatbot API endpoint
@app.post("/chat/")
async def chat(request: ChatRequest):
    try:
        # Convert messages into the correct format for the AI
        messages = [(msg["role"], msg["content"]) for msg in request.messages]

        response = llm.invoke(messages)
        return {"response": response.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")
