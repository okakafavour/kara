from app.profiles.models import (
    BrowserProfile,
    Workspace,
)
from app.profiles.storage import ProfileStorage


class ProfileManager:
    """
    Manages browser profiles and workspaces.
    """

    def __init__(self):

        self.storage = ProfileStorage()

        self.browser_profiles = []

        self.workspaces = []

        self.load()

    def load(self):

        data = self.storage.load()

        self.browser_profiles = [

            BrowserProfile(**profile)

            for profile in data.get(
                "browser_profiles",
                [],
            )
        ]

        self.workspaces = [

            Workspace(**workspace)

            for workspace in data.get(
                "workspaces",
                [],
            )
        ]

    def get_browser_profile(self, name: str):

        for profile in self.browser_profiles:

            if profile.name.lower() == name.lower():

                return profile

        return None

    def get_workspace(self, name: str):

        for workspace in self.workspaces:

            if workspace.name.lower() == name.lower():

                return workspace

        return None

    def browser_profiles_list(self):

        return self.browser_profiles

    def workspaces_list(self):

        return self.workspaces