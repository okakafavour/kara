from dataclasses import dataclass


@dataclass
class ExecutionResult:
    success: bool
    message: str
    step: dict | None = None