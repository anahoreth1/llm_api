def get_llm_client(llm_type: str):

    if llm_type == "gemini":
        from src.llm.gemini_client import GeminiClient

        return GeminiClient()
    elif llm_type == "mock":
        from src.llm.mock_client import MockClient

        return MockClient()
    else:
        raise ValueError(f"Unsupported LLM type: {llm_type}")
