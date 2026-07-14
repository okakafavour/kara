from app.skills.manager import SkillManager

manager = SkillManager()

tests = [
    {
        "intent": "open_application",
        "entities": {
            "application": "firefox",
        },
    },
    {
        "intent": "browser_open",
        "entities": {
            "url": "github.com",
        },
    },
]

print("=" * 40)
print("Testing Skill Manager")
print("=" * 40)

for task in tests:

    print("\nTask:")
    print(task)

    result = manager.execute(task)

    print("Result:")
    print(result)

input("\nPress Enter to close the browser...")

# Close browser if it is still open
manager.execute(
    {
        "intent": "browser_close",
        "entities": {},
    }
)

print("\nSkill Manager Test Complete")