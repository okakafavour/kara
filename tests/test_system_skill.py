from app.skills.system.system_skill import SystemSkill

skill = SystemSkill()

tasks = [
    {"intent": "battery_status"},
    {"intent": "cpu_status"},
    {"intent": "memory_status"},
    {"intent": "disk_status"},
]

print("=" * 40)
print("Testing System Skill")
print("=" * 40)

for task in tasks:

    print()
    print(task["intent"])

    result = skill.execute(task)

    print(result)