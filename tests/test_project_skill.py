
from app.skills.project.project_skill import ProjectSkill

print("=" * 40)
print("Project Skill Test")
print("=" * 40)

skill = ProjectSkill()

result = skill.execute(
    {
        "intent": "continue_project",
        "entities": {
            "project": "Uber",
        },
    }
)

print(result)