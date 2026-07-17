from app.decision.models import Decision
from app.decision.rules.base import BaseDecisionRule


class RunningAppsRule(BaseDecisionRule):
    """
    Prevent opening applications that are already running.
    """

    def applies(self, plan, session):

        return any(
            step.intent == "open_application"
            for step in plan.steps
        )

    def decide(self, plan, session):

        for step in plan.steps:

            if step.intent != "open_application":
                continue

            app = step.entities["application"]

            if session.is_running(app):

                return Decision(
                    proceed=False,
                    requires_confirmation=True,
                    question=f"{app} is already running. Open another window?"
                )

        return Decision()