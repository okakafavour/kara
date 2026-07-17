from app.planner.models.plan import ExecutionPlan
from app.planner.models.step import Step
from app.planner.rules.base import BasePlanningRule


class BrowserRule(BasePlanningRule):

    @property
    def intents(self):
        return [
            "browser_open",
            "browser_search",
            "browser_close",
        ]

    def expand(self, task):

        entities = task.get("entities", {})

        intent = task["intent"]

        if intent == "browser_open":

            return ExecutionPlan(
                goal=f"Open {entities['url']}",
                steps=[
                    Step(
                        intent="open_application",
                        entities={
                            "application": entities.get(
                                "browser",
                                "firefox",
                            )
                        },
                    ),
                    Step(
                        intent="browser_open",
                        entities={
                            "url": entities["url"]
                        },
                    ),
                ],
            )

        return ExecutionPlan(
            goal=intent,
            steps=[
                Step(
                    intent=intent,
                    entities=entities,
                )
            ],
        )