from app.decision.engine import DecisionEngine
from app.planner.models.plan import ExecutionPlan
from app.planner.models.step import Step
from app.session.manager import SessionManager

print("=" * 40)
print("Testing Decision Engine")
print("=" * 40)

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

engine = DecisionEngine()

decision = engine.evaluate(
    plan,
    session,
)

print(decision)