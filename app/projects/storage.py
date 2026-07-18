import json
from pathlib import Path

from app.projects.models import Project
from dataclasses import asdict


class ProjectStorage:
    """
    Handles reading and writing projects
    from permanent storage.
    """

    def __init__(self):

        self.path = Path("data/projects.json")

        self.path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        if not self.path.exists():

            self.path.write_text(
                "[]",
                encoding="utf-8",
            )

    # ----------------------------------

    def load(self) -> list[Project]:
        """
        Load every stored project.
        """

        data = json.loads(
            self.path.read_text(
                encoding="utf-8"
            )
        )

        return [
            Project(**item)
            for item in data
        ]

    # ----------------------------------

    def save(
        self,
        projects: list[Project],
    ):
        """
        Save every project.
        """

        data = [
            asdict(project)
            for project in projects
        ]

        self.path.write_text(
            json.dumps(
                data,
                indent=4,
            ),
            encoding="utf-8",
        )