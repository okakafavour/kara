from abc import ABC, abstractmethod


class BaseSkill(ABC):
    """
    Base class for every Kara skill.

    Every skill advertises:
    - who it is
    - what it can do
    - which intents it supports
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """Unique skill name."""
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        """Human-readable description."""
        pass

    @property
    @abstractmethod
    def intents(self) -> list[str]:
        """Supported intents."""
        pass

    @abstractmethod
    def can_handle(self, task: dict) -> bool:
        """Return True if this skill can execute the task."""
        pass

    @abstractmethod
    def execute(self, task: dict):
        """Execute a task."""
        pass

    def metadata(self) -> dict:
        """
        Metadata used by the Skill Manager
        and Prompt Builder.
        """
        return {
            "name": self.name,
            "description": self.description,
            "intents": self.intents,
        }