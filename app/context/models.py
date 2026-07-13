from dataclasses import dataclass, field


@dataclass
class ContextModel:
    current_application: str | None = None
    current_website: str | None = None
    current_directory: str | None = None

    last_intent: str | None = None
    last_tool: str | None = None

    conversation: list[str] = field(default_factory=list)

    working_memory: dict = field(default_factory=dict)