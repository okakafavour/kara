from dataclasses import dataclass, field


@dataclass
class ApplicationSession:
    application: str
    running: bool = False


@dataclass
class BrowserTab:
    title: str
    url: str


@dataclass
class BrowserSession:
    browser: str
    tabs: list[BrowserTab] = field(default_factory=list)


@dataclass
class WorkspaceSession:
    name: str | None = None


@dataclass
class SessionState:
    applications: dict[str, ApplicationSession] = field(default_factory=dict)
    browsers: dict[str, BrowserSession] = field(default_factory=dict)
    workspace: WorkspaceSession = field(default_factory=WorkspaceSession)