from abc import ABC, abstractmethod

from app.decision.models import Decision


class BaseDecisionRule(ABC):
    """
    Base class for every decision rule.
    """

    @abstractmethod
    def applies(self, plan, session) -> bool:
        """
        Whether this rule should inspect the plan.
        """
        pass

    @abstractmethod
    def decide(self, plan, session) -> Decision:
        """
        Return the decision.
        """
        pass