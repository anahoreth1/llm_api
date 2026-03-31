from functools import lru_cache


@lru_cache
def get_llm_client(llm_type: str):
    if llm_type == "gemini":
        from src.llm.gemini_client import GeminiClient

        return GeminiClient()

    if llm_type == "mock":
        from src.llm.mock_client import MockClient

        return MockClient()

    raise ValueError(f"Unsupported LLM type: {llm_type}")
