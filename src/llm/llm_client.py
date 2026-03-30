from abc import ABC, abstractmethod


class LLMCallResult:
    def __init__(
        self, response: str = "", tokens_used: int = 0, cached: bool = False
    ) -> None:
        self.response = response
        self.tokens_used = tokens_used
        self.cached = cached


class LLMClient(ABC):
    def __init__(self):
        self.model_name = ""

    @abstractmethod
    def generate_content(self, prompt) -> LLMCallResult:
        # Placeholder for actual LLM response generation logic
        print(
            f"Generated response for prompt: '{prompt}' using model: '{self.model_name}'"
        )

        return LLMCallResult()
