from fastapi import APIRouter, Depends
from pydantic import BaseModel

from src.dependencies.services import get_llm_service
from src.services.llm_service import LLMService
from src.llm.llm_client import LLMCallResult

router = APIRouter()


class PromptRequest(BaseModel):
    prompt: str


@router.post("/generate")
async def generate(
    req: PromptRequest, llm_service: LLMService = Depends(get_llm_service)
):
    llm_call_result: LLMCallResult = await llm_service.generate_response(
        prompt=req.prompt
    )

    return {
        "status": "ok",
        "response": llm_call_result.response,
        "meta": {
            "cached": llm_call_result.cached,
            "tokens_used": llm_call_result.tokens_used,
        },
    }
