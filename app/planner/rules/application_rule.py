from app.planner.models.plan import ExecutionPlan
from app.planner.models.step import Step
from app.planner.rules.base import BasePlanningRule


class ApplicationRule(BasePlanningRule):

    @property
    def intents(self):
        return [
            "open_application",
        ]

    def expand(self, task):

        entities = task.get("entities", {})

        return ExecutionPlan(
            goal=f"Open {entities.get('application')}",
            steps=[
                Step(
                    intent="open_application",
                    entities=entities,
                )
            ],
        )