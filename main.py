from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict, Optional

app = FastAPI()

class ContextRequest(BaseModel):
    context_keys: List[str]
    request: Optional[Dict] = None

class ContextItem(BaseModel):
    key: str
    content: str

class ContextResponse(BaseModel):
    contexts: List[ContextItem]

@app.post("/v1/context")
async def get_context(data: ContextRequest):
    context_map = {
        "faq": "Support is available from 9AM–5PM, Monday to Friday.",
        "client_profile:123": "Client 123 is a premium user since Jan 2022."
    }

    response_contexts = [
        ContextItem(key=key, content=context_map.get(key, "No content found."))
        for key in data.context_keys
    ]
    return {"contexts": [c.dict() for c in response_contexts]}
