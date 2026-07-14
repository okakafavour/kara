from playwright.sync_api import Error, sync_playwright

from app.skills.browser.actions import BrowserActions


class BrowserEngine:
    """
    Controls a persistent Playwright browser session.
    """

    def __init__(self):
        self.playwright = None
        self.browser = None
        self.page = None
        self.actions = None

    def start(self):
        """
        Start the browser if necessary.
        """

        if self.browser is None:

            print("\n===== STARTING PLAYWRIGHT =====")

            self.playwright = sync_playwright().start()

            self.browser = self.playwright.firefox.launch(
                headless=False
            )

            self.page = self.browser.new_page()

            self.actions = BrowserActions(self)

            print("Playwright:", self.playwright)
            print("Browser:", self.browser)
            print("Page:", self.page)
            print("===============================\n")

            return

        if self.page is None:

            print("\n===== CREATING NEW PAGE =====")

            self.page = self.browser.new_page()

            self.actions = BrowserActions(self)

            print("Page:", self.page)
            print("=============================\n")

    def goto(self, url: str):
        """
        Navigate to a URL.
        """

        self.start()

        if not url.startswith(("http://", "https://")):
            url = "https://" + url

        try:

            self.page.goto(url)

        except Error as error:

            print("\nPlaywright Error:", error)
            print("Restarting browser...\n")

            self.close()

            self.start()

            self.page.goto(url)

    def title(self):

        if self.page:
            return self.page.title()

        return ""

    def current_url(self):

        if self.page:
            return self.page.url

        return ""

    def close(self):

        try:
            if self.browser:
                self.browser.close()
        except Exception:
            pass

        try:
            if self.playwright:
                self.playwright.stop()
        except Exception:
            pass

        self.browser = None
        self.page = None
        self.playwright = None
        self.actions = None