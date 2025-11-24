from pydantic import BaseModel
from typing import List
from fastapi import FastAPI
from ai_agent import get_response_from_agent
import uvicorn

class Request(BaseModel):
    model_provider:str
    model_name:str
    messages:List[str]
    allow_search:bool

app = FastAPI()
ALLOWED_MODEL_NAMES = ["gemini-2.5-flash", "llama-3.3-70b-versatile", "llama-3.1-8b-instant"]

@app.post("/generate")
def generate(request: Request):
    if request.model_name not in ALLOWED_MODEL_NAMES:
        return {"error": "Model not allowed"}
    
    response = get_response_from_agent(
        llm_name=request.model_name,
        provider=request.model_provider,
        prompt=request.messages,
        allow_search=request.allow_search
    )

    return response

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    
