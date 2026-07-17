from app.conversation.manager import ConversationManager
from app.planner.models.plan import ExecutionPlan

print("=" * 40)
print("Conversation Manager Test")
print("=" * 40)

manager = ConversationManager()

plan = ExecutionPlan(
    goal="Open Firefox",
    steps=[],
)

manager.ask_confirmation(
    plan=plan,
    question="Firefox is already running. Open another window?",
)

print()

print("Waiting?")
print(manager.waiting())

print()

print("Pending Action")
print(manager.pending())

manager.clear()

print()

print("Waiting After Clear?")
print(manager.waiting())