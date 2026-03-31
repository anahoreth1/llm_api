import time

from src.llm.client_factory import get_llm_client
from src.llm.llm_client import LLMCallResult
from src.consts import RETRIES_COUNT


class LLMServiceError(Exception):
    pass


class LLMService:
    def __init__(self, client_type) -> None:
        self.client = get_llm_client(client_type)
        self._cache = {}
        self._ttl = 60

    def _make_cache_key(self, prompt: str):
        return prompt

    async def generate_response(self, prompt: str) -> LLMCallResult:
        key = self._make_cache_key(prompt)

        if key in self._cache:
            timestamp, call_result = self._cache[key]
            now = time.time()
            print(now, timestamp, now - timestamp)
            if now - timestamp < self._ttl:
                call_result.cached = True
                return call_result

        call_number = 0
        call_result: LLMCallResult = LLMCallResult()
        while call_number < RETRIES_COUNT:
            try:
                call_result: LLMCallResult = await self.client.generate_content(
                    prompt=prompt
                )
                break

            except Exception as e:
                print(f"Retry {call_number}: {e}")
                call_number += 1
        if call_number == RETRIES_COUNT:
            raise LLMServiceError("LLM failed after retries")

        now = time.time()
        self._cache[key] = (now, call_result)
        return call_result
