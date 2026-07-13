from playwright.sync_api import sync_playwright


class BrowserEngine:
    """
    Controls a Playwright browser instance.

    The engine keeps one browser alive so Kara can
    continue working in the same browsing session.
    """

    def __init__(self):
        self.playwright = None
        self.browser = None
        self.page = None

    def start(self):
        """
        Start the browser if it isn't already running.
        """

        if self.browser is not None:
            return

        self.playwright = sync_playwright().start()

        self.browser = self.playwright.firefox.launch(
            headless=False
        )

        self.page = self.browser.new_page()

    def goto(self, url: str):
        """
        Navigate to a URL.
        """

        self.start()

        if not url.startswith(("http://", "https://")):
            url = "https://" + url

        self.page.goto(url)

    def title(self):
        """
        Return the current page title.
        """

        if self.page:
            return self.page.title()

        return ""

    def current_url(self):
        """
        Return the current page URL.
        """

        if self.page:
            return self.page.url

        return ""

    def close(self):
        """
        Close the browser cleanly.
        """

        if self.browser:
            self.browser.close()

        if self.playwright:
            self.playwright.stop()

        self.browser = None
        self.page = None
        self.playwright = None