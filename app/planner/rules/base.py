from abc import ABC, abstractmethod

from app.planner.models.plan import ExecutionPlan


class BasePlanningRule(ABC):
    """
    Base class for every planning rule.
    """

    @property
    @abstractmethod
    def intents(self) -> list[str]:
        """
        Intents handled by this rule.
        """
        pass

    @abstractmethod
    def expand(self, task: dict) -> ExecutionPlan:
        """
        Convert a task into an execution plan.
        """
        pass