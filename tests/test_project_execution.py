# tests/test_project_execution.py

from app.execution.engine import ExecutionEngine
from app.planner.models.plan import ExecutionPlan
from app.planner.models.step import Step
from app.context.context import ContextManager
from app.session.manager import SessionManager
from app.skills.manager import SkillManager
from app.response.formatter import ResponseFormatter

print("=" * 40)
print("Project Execution Test")
print("=" * 40)

engine = ExecutionEngine(
    skill_manager=SkillManager(),
    context=ContextManager(),
    session=SessionManager(),
)

formatter = ResponseFormatter()

plan = ExecutionPlan(
    goal="Continue Uber",
    steps=[
        Step(
            intent="continue_project",
            entities={
                "project": "Uber",
            },
        )
    ],
)

results = engine.execute(plan)

print("\nRaw Results\n")
print(results)

print("\nFormatted\n")
print(formatter.format(results))