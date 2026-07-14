from app.skills.manager import SkillManager

print("=" * 40)
print("Testing Skill Metadata")
print("=" * 40)

manager = SkillManager()

print("\nInstalled Skills\n")

for skill in manager.metadata():
    print(skill)

print("\nSupported Intents\n")

print(manager.intents())

print("\nMetadata Test Complete")