from dataclasses import dataclass


@dataclass
class BrowserProfile:
    """
    Represents a browser profile.
    """

    name: str

    browser: str

    email: str

    profile_path: str | None = None

    startup_url: str | None = None


@dataclass
class Workspace:
    """
    Represents a complete working environment.
    """

    name: str

    browser_profile: str

    applications: list[str]

    startup_urls: list[str]