from fastapi import APIRouter
from pydantic import BaseModel

from src.services.llm import generate_response

router = APIRouter()


class PromptRequest(BaseModel):
    prompt: str


@router.get("/health")
async def health_check():
    return {"status": "ok", "response": "LLM API is healthy and running!"}


@router.post("/generate")
async def generate(req: PromptRequest):
    result = await generate_response(prompt=req.prompt)
    return {"status": "ok", "response": result}
