from dataclasses import dataclass, field


@dataclass(slots=True)
class ActionResult:
    """
    Structured result returned by a skill.

    This replaces plain English strings and allows the
    ResponseFormatter to generate user-facing text.
    """

    action: str

    success: bool = True

    payload: dict = field(default_factory=dict)

    error: str | None = None