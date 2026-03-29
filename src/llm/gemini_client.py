import google.generativeai as genai

from src.llm.llm_client import LLMClient
from src.consts import GEMINI_API_KEY, gemini_model_name


class GeminiClient(LLMClient):
    def __init__(self):
        genai.configure(api_key=GEMINI_API_KEY)
        self.model_name = gemini_model_name
        self.gemini = genai.GenerativeModel(gemini_model_name)

    def generate_content(self, prompt) -> str:
        super().generate_content(prompt)

        response = self.gemini.generate_content(prompt)
        return response.text
