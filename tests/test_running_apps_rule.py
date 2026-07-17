from app.decision.rules.running_apps import RunningAppsRule
from app.planner.models.plan import ExecutionPlan
from app.planner.models.step import Step
from app.session.manager import SessionManager

session = SessionManager()

session.application_started("firefox")

plan = ExecutionPlan(
    goal="Open Firefox",
    steps=[
        Step(
            intent="open_application",
            entities={
                "application": "firefox"
            }
        )
    ]
)

rule = RunningAppsRule()

decision = rule.decide(plan, session)

print("=" * 40)
print("Running Apps Decision")
print("=" * 40)

print(decision)