from dataclasses import dataclass
from typing import Any


@dataclass
class LLMRequest:
    prompt: str
    model: str = "qwen2.5:1.5b"


@dataclass
class LLMResponse:
    success: bool
    content: str
    raw: Any = None
    error: str | None = None