from dataclasses import dataclass, field
from typing import Optional


@dataclass
class BrowserProfile:
    """
    Represents a browser profile.
    """

    name: str
    browser: str
    email: Optional[str] = None
    profile_path: Optional[str] = None


@dataclass
class BrowserSession:
    """
    Represents one running browser session.
    """

    browser: str

    profile: Optional[BrowserProfile] = None

    playwright = None
    browser_instance = None
    context = None
    page = None

    active: bool = False

    tabs: list = field(default_factory=list)