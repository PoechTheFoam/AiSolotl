from typing import Any 
from fastapi import FastAPI
from pydantic import BaseModel 
from fastapi.middleware.cors import CORSMiddleware
from summarizer import summarize
from datetime import date


app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://www.facebook.com"],
    allow_methods=["POST","OPTIONS"],
    allow_headers=["Content-Type"]
)

class ExtractionPayload(BaseModel):
    platform:str 
    conversations:dict[str,Any]

@app.get('/health')
def health() -> dict[str,str]:
    return {"status": "ok"}

@app.post("/echo")
def echo_extraction(payload: ExtractionPayload) -> dict[str, Any]:
     return {
        "ok": True,
        "platform": payload.platform,
        "conversations": payload.conversations
    }

@app.post("/summarize")
async def summarization_layer(payload: ExtractionPayload):
    ref_time=date.today()
    result=summarize(payload.conversations,ref_time)
    
    return {"ok":True,
            "result":result} #used for display later