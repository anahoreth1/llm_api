from functools import lru_cache
from src.services.llm_service import LLMService
from src.consts import CLIENT_TYPE


@lru_cache
def get_llm_service() -> LLMService:
    return LLMService(CLIENT_TYPE)
