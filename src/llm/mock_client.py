from src.llm.llm_client import LLMClient


class MockClient(LLMClient):
    def __init__(self):
        self.model_name = "MockClient"

    def generate_content(self, prompt) -> str:
        super().generate_content(prompt)
        mock_content = "It is a mock content from the LLM"
        return mock_content
