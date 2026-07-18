from dataclasses import dataclass, field


@dataclass(slots=True)
class Project:
    """
    Represents a project Kara manages.
    """

    name: str

    description: str = ""

    path: str = ""

    github: str = ""

    backend: str = ""

    frontend: str = ""

    database: str = ""

    workspace: str = ""

    branch: str = "main"

    status: str = "active"

    last_task: str = ""

    next_task: str = ""

    notes: list[str] = field(default_factory=list)