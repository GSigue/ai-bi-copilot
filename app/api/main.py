from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI
from pydantic import BaseModel
from app.ai.llm_engine import ask_ai

app = FastAPI(title="AI BI Copilot", version="1.0")

# ------------------------
# REQUEST MODEL
# ------------------------
class QueryRequest(BaseModel):
    question: str


# ------------------------
# HEALTH CHECK
# ------------------------
@app.get("/")
def home():
    return {"status": "AI BI Copilot running"}


# ------------------------
# MAIN ENDPOINT
# ------------------------
@app.post("/ask")
def ask_question(req: QueryRequest):
    result = ask_ai(req.question)
    return result