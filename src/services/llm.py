def get_llm_client(llm_type):

    if llm_type == "gemini":
        from src.llm.gemini_client import GeminiClient

        return GeminiClient()
    elif llm_type == "mock":
        from src.llm.mock_client import MockClient

        return MockClient()
    else:
        raise ValueError(f"Unsupported LLM type: {llm_type}")


llm_client = get_llm_client("mock")


async def generate_response(prompt: str) -> str:
    text_content = llm_client.generate_content(prompt=prompt)
    return text_content
