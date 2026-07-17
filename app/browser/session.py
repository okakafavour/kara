from playwright.sync_api import Error, sync_playwright

from app.browser.models import BrowserProfile, BrowserSession as BrowserSessionModel
from app.browser.actions import BrowserActions


class BrowserSession:
    """
    Controls one persistent browser session.
    """

    def __init__(
        self,
        browser: str = "firefox",
        profile: BrowserProfile | None = None,
    ):
        self.model = BrowserSessionModel(
            browser=browser,
            profile=profile,
        )

    @property
    def page(self):
        return self.model.page

    def start(self):
        """
        Start the browser if it isn't already running.
        """

        if self.model.browser_instance is not None:
            return

        self.model.playwright = sync_playwright().start()

        browser_name = self.model.browser.lower()

        if browser_name == "firefox":

            self.model.browser_instance = (
                self.model.playwright.firefox.launch(
                    headless=False
                )
            )

        elif browser_name == "chromium":

            self.model.browser_instance = (
                self.model.playwright.chromium.launch(
                    headless=False
                )
            )

        elif browser_name == "chrome":

            self.model.browser_instance = (
                self.model.playwright.chromium.launch(
                    channel="chrome",
                    headless=False
                )
            )

        else:
            raise ValueError(
                f"Unsupported browser: {browser_name}"
            )

        self.model.context = (
            self.model.browser_instance.new_context()
        )

        self.model.page = self.model.context.new_page()

        self.actions = BrowserActions(self)

        self.model.active = True

    def goto(self, url: str):

        self.start()

        if not url.startswith(("http://", "https://")):
            url = "https://" + url

        try:
            self.model.page.goto(url)

        except Error:

            self.close()

            self.start()

            self.model.page.goto(url)

    def title(self):

        if self.model.page:
            return self.model.page.title()

        return ""

    def current_url(self):

        if self.model.page:
            return self.model.page.url

        return ""

    def close(self):

        try:

            if self.model.browser_instance:
                self.model.browser_instance.close()

        except Exception:
            pass

        try:

            if self.model.playwright:
                self.model.playwright.stop()

        except Exception:
            pass

        self.model.browser_instance = None
        self.model.context = None
        self.model.page = None
        self.model.playwright = None
        self.model.active = False