from src.llm.llm_client import LLMClient, LLMCallResult


class MockClient(LLMClient):
    def __init__(self):
        self.model_name = "MockClient"

    def generate_content(self, prompt) -> LLMCallResult:
        super().generate_content(prompt)
        mock_content = "It is a mock content from the LLM"
        call_result = LLMCallResult(mock_content, 0, False)
        return call_result
