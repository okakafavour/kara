from app.conversation.manager import ConversationManager
from app.planner.models.plan import ExecutionPlan

print("=" * 40)
print("Conversation Reply Test")
print("=" * 40)

manager = ConversationManager()

manager.ask_confirmation(
    ExecutionPlan(goal="Demo", steps=[]),
    "Continue?",
)

commands = [
    "yes",
    "ok",
    "go ahead",
    "cancel",
    "no",
    "hello",
]

for command in commands:
    print(f"\n{command}")

    print("Is reply:", manager.is_reply(command))
    print("Resolved:", manager.resolve_reply(command))