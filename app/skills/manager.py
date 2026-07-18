from rich.console import Console

from app.plugins.loader import PluginLoader
from app.skills.base import BaseSkill

console = Console()


class SkillManager:
    """
    Automatically discovers and manages every Kara skill.
    """

    def __init__(self):
        self.skills = []
        self.load_skills()

    def load_skills(self):
        """
        Discover every installed skill.
        """

        self.skills = PluginLoader.load(
            "app.skills",
            BaseSkill,
        )

        for skill in self.skills:
            console.log(
                f"[green]Loaded Skill:[/green] {skill.name}"
            )

    def execute(self, task: dict):
        """
        Execute the first skill that can handle the task.
        """

        for skill in self.skills:

            if skill.can_handle(task):
                return skill.execute(task)

        return "I don't know how to do that yet."

    def metadata(self):
        """
        Return metadata for every installed skill.
        """

        return [
            skill.metadata()
            for skill in self.skills
        ]

    def intents(self):
        """
        Return every supported intent.
        """

        intents = []

        for skill in self.skills:
            intents.extend(skill.intents)

        return sorted(set(intents))

    def find_skill(self, intent: str):
        """
        Find the skill responsible for an intent.
        """

        for skill in self.skills:

            if intent in skill.intents:
                return skill

        return None
