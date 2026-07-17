from app.context.context import ContextManager
from app.execution.engine import ExecutionEngine
from app.planner.models.plan import ExecutionPlan
from app.planner.models.step import Step
from app.session.manager import SessionManager
from app.skills.manager import SkillManager

print("=" * 40)
print("Execution Decision Test")
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
            },
        )
    ],
)

engine = ExecutionEngine(
    skill_manager=SkillManager(),
    context=ContextManager(),
    session=session,
)

results = engine.execute(plan)

for result in results:
    print(result)