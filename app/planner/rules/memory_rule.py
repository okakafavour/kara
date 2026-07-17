from app.planner.models.plan import ExecutionPlan
from app.planner.models.step import Step
from app.planner.rules.base import BasePlanningRule


class MemoryRule(BasePlanningRule):

    @property
    def intents(self):
        return [
            "remember",
            "recall",
        ]

    def expand(self, task):

        return ExecutionPlan(
            goal=task["intent"],
            steps=[
                Step(
                    intent=task["intent"],
                    entities=task.get("entities", {}),
                )
            ],
        )