from app.projects.manager import ProjectManager


class ProjectContext:
    """
    Keeps track of Kara's current project and
    helps resolve project-related questions.
    """

    def __init__(self):

        self.manager = ProjectManager()

        self.current_project = None

    # ----------------------------------

    def current(self):

        return self.current_project

    # ----------------------------------

    def set_current(self, name: str):

        project = self.manager.get(name)

        if project is None:
            return None

        self.current_project = project

        return project

    # ----------------------------------

    def clear(self):

        self.current_project = None

    # ----------------------------------

    def find(self, name: str):

        return self.manager.get(name)