from src.llm.client_factory import get_llm_client

from src.llm.llm_client import LLMCallResult


class LLMService:
    def __init__(self, client_type) -> None:
        self.client = get_llm_client(client_type)

    async def generate_response(self, prompt: str) -> LLMCallResult:
        call_result: LLMCallResult = self.client.generate_content(prompt=prompt)

        return call_result
