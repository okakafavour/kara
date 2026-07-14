import importlib
import inspect
import pkgutil

from rich.console import Console

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

        package = importlib.import_module("app.skills")

        for _, package_name, is_package in pkgutil.iter_modules(package.__path__):

            if not is_package:
                continue

            package_path = f"app.skills.{package_name}"

            package_module = importlib.import_module(package_path)

            for _, module_name, _ in pkgutil.iter_modules(package_module.__path__):

                if module_name.startswith("__"):
                    continue

                module = importlib.import_module(
                    f"{package_path}.{module_name}"
                )

                for _, obj in inspect.getmembers(module, inspect.isclass):

                    if (
                        issubclass(obj, BaseSkill)
                        and obj is not BaseSkill
                    ):

                        skill = obj()

                        console.log(
                            f"[green]Loaded Skill:[/green] {skill.name}"
                        )

                        self.skills.append(skill)

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