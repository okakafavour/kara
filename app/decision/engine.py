from app.decision.models import Decision
from app.decision.registry import DecisionRegistry


class DecisionEngine:
    """
    Evaluates an execution plan before it is executed.
    """

    def __init__(self):

        self.registry = DecisionRegistry()

    def evaluate(
        self,
        plan,
        session,
    ):

        rules = self.registry.applicable_rules(
            plan,
            session,
        )

        for rule in rules:

            decision = rule.decide(
                plan,
                session,
            )

            if not decision.proceed:

                return decision

        return Decision()