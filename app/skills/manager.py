from app.skills.applications.application_skill import ApplicationSkill


class SkillManager:
    """
    Routes execution requests to the appropriate skill.
    """

    def __init__(self):
        self.application = ApplicationSkill()

    def execute(self, task: dict):

        intent = task.get("intent")

        if intent == "open_application":
            return self.application.open(task.get("target"))

        return "I don't know how to perform that action yet."