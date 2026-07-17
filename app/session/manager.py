from app.session.models import (
    ApplicationSession,
    BrowserSession,
    BrowserTab,
    SessionState,
)


class SessionManager:
    """
    Tracks Kara's current desktop session.
    """

    def __init__(self):

        self.state = SessionState()

    # -------------------------
    # Applications
    # -------------------------

    def application_started(self, application: str):

        self.state.applications[application] = ApplicationSession(
            application=application,
            running=True,
        )

    def is_running(self, application: str):

        session = self.state.applications.get(application)

        if session is None:
            return False

        return session.running

    # -------------------------
    # Browsers
    # -------------------------

    def browser_opened(self, browser: str):

        if browser not in self.state.browsers:

            self.state.browsers[browser] = BrowserSession(
                browser=browser,
            )

    def browser_tab(self, browser: str, title: str, url: str):

        self.browser_opened(browser)

        self.state.browsers[browser].tabs.append(
            BrowserTab(
                title=title,
                url=url,
            )
        )

    # -------------------------
    # Workspace
    # -------------------------

    def workspace_started(self, name: str):

        self.state.workspace.name = name

    # -------------------------

    def current_workspace(self):

        return self.state.workspace.name
    
    def is_running(self, application: str) -> bool:
        """
        Check whether an application is already running.
        """

        return application.lower() in {
            app.lower()
            for app in self.state.applications
        }