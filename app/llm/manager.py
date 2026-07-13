from app.llm.client import LLMClient
from app.llm.models import LLMRequest, LLMResponse


class LLMManager:
    """
    High-level interface used by the Brain.
    """

    def __init__(self):
        self.client = LLMClient()

    def ask(self, prompt: str) -> LLMResponse:
        request = LLMRequest(prompt=prompt)
        return self.client.generate(request)