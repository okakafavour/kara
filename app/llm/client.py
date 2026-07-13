from ollama import Client

from app.llm.models import LLMRequest, LLMResponse


class LLMClient:
    """
    Low-level client responsible for communicating with Ollama.
    """

    def __init__(
        self,
        host: str = "http://127.0.0.1:11434",
    ):
        self.client = Client(host=host)

    def generate(self, request: LLMRequest) -> LLMResponse:
        """
        Send a prompt to the configured Ollama model.
        """

        try:
            response = self.client.chat(
                model=request.model,
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are the reasoning engine for Kara AI."
                        ),
                    },
                    {
                        "role": "user",
                        "content": request.prompt,
                    },
                ],
            )

            return LLMResponse(
                success=True,
                content=response["message"]["content"],
                raw=response,
            )

        except Exception as error:
            return LLMResponse(
                success=False,
                content="",
                error=str(error),
            )