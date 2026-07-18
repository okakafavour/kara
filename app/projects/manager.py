from app.projects.models import Project
from app.projects.storage import ProjectStorage


class ProjectManager:
    """
    Manages Kara's projects.
    """

    def __init__(self):

        self.storage = ProjectStorage()
        self.projects = self.storage.load()

    # ----------------------------------
    # Query Methods
    # ----------------------------------

    def list(self) -> list[Project]:
        """
        Return every project.
        """
        return self.projects

    # ----------------------------------

    def exists(self, name: str) -> bool:
        """
        Check whether a project exists.
        """
        name = name.lower()

        return any(
            project.name.lower() == name
            for project in self.projects
        )

    # ----------------------------------

    def get(self, name: str):

        name = name.lower()

        for project in self.projects:

            if project.name.lower() == name:
                return project

        return None

    # ----------------------------------
    # CRUD
    # ----------------------------------

    def create(self, project: Project):

        if self.exists(project.name):
            raise ValueError(
                f"Project '{project.name}' already exists."
            )

        self.projects.append(project)

        self.storage.save(self.projects)

        return project

    # ----------------------------------

    def delete(self, name: str) -> bool:

        project = self.get(name)

        if project is None:
            return False

        self.projects.remove(project)

        self.storage.save(self.projects)

        return True

    # ----------------------------------

    def update(self, project: Project):

        for index, current in enumerate(self.projects):

            if current.name.lower() == project.name.lower():

                self.projects[index] = project

                self.storage.save(self.projects)

                return project

        raise ValueError(
            f"Project '{project.name}' does not exist."
        )

    # ----------------------------------
    # Project Helpers
    # ----------------------------------

    def rename(
        self,
        old_name: str,
        new_name: str,
    ):

        if self.exists(new_name):
            raise ValueError(
                f"Project '{new_name}' already exists."
            )

        project = self.get(old_name)

        if project is None:
            raise ValueError(
                f"Project '{old_name}' does not exist."
            )

        project.name = new_name

        self.storage.save(self.projects)

        return project

    # ----------------------------------

    def set_path(
        self,
        name: str,
        path: str,
    ):

        project = self.get(name)

        if project is None:
            raise ValueError(
                f"Project '{name}' does not exist."
            )

        project.path = path

        self.storage.save(self.projects)

        return project

    # ----------------------------------

    def set_github(
        self,
        name: str,
        github: str,
    ):

        project = self.get(name)

        if project is None:
            raise ValueError(
                f"Project '{name}' does not exist."
            )

        project.github = github

        self.storage.save(self.projects)

        return project

    # ----------------------------------

    def set_workspace(
        self,
        name: str,
        workspace: str,
    ):

        project = self.get(name)

        if project is None:
            raise ValueError(
                f"Project '{name}' does not exist."
            )

        project.workspace = workspace

        self.storage.save(self.projects)

        return project

    # ----------------------------------

    def set_branch(
        self,
        name: str,
        branch: str,
    ):

        project = self.get(name)

        if project is None:
            raise ValueError(
                f"Project '{name}' does not exist."
            )

        project.branch = branch

        self.storage.save(self.projects)

        return project

    # ----------------------------------

    def set_last_task(
        self,
        name: str,
        task: str,
    ):

        project = self.get(name)

        if project is None:
            raise ValueError(
                f"Project '{name}' does not exist."
            )

        project.last_task = task

        self.storage.save(self.projects)

        return project

    # ----------------------------------

    def set_next_task(
        self,
        name: str,
        task: str,
    ):

        project = self.get(name)

        if project is None:
            raise ValueError(
                f"Project '{name}' does not exist."
            )

        project.next_task = task

        self.storage.save(self.projects)

        return project

    # ----------------------------------

    def add_note(
        self,
        name: str,
        note: str,
    ):

        project = self.get(name)

        if project is None:
            raise ValueError(
                f"Project '{name}' does not exist."
            )

        project.notes.append(note)

        self.storage.save(self.projects)

        return project