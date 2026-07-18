from app.conversation.manager import ConversationManager
from app.planner.models.plan import ExecutionPlan

print("=" * 40)
print("Conversation Resume Test")
print("=" * 40)

conversation = ConversationManager()

plan = ExecutionPlan(
    goal="Open Firefox",
    steps=[],
)

conversation.ask_confirmation(
    plan,
    "Firefox is already running. Open another window?",
)

print()

print("Waiting?")
print(conversation.waiting())

print()

print("Confirming...")

returned = conversation.confirm()

print(returned)

print()

print("Waiting?")
print(conversation.waiting())