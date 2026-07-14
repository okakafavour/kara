from app.brain.brain import Brain

print("=" * 40)
print("Testing Brain")
print("=" * 40)

brain = Brain()

commands = [
    "open firefox",
    "remember my name is Favour",
    "what is my name",
    "Could you launch Firefox?",
    "Please open GitHub",
]

for command in commands:

    print(f"\nCommand: {command}")

    task = brain.process(command)

    print(task)

print("\nBrain Test Complete")