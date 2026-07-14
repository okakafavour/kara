from playwright.sync_api import TimeoutError


class BrowserActions:
    """
    Common browser actions used by Kara.
    """

    def __init__(self, browser_engine):
        self.browser = browser_engine

    def click(self, selector: str):
        """
        Click an element.
        """
        locator = self.browser.page.locator(selector)
        locator.click()

    def type(self, selector: str, text: str):
        """
        Type text into an input field.
        """
        locator = self.browser.page.locator(selector)
        locator.fill(text)

    def press(self, selector: str, key: str):
        """
        Press a keyboard key on an element.
        """
        locator = self.browser.page.locator(selector)
        locator.press(key)

    def wait_for(self, selector: str, timeout: int = 10000):
        """
        Wait until an element appears.
        """
        locator = self.browser.page.locator(selector)
        locator.wait_for(timeout=timeout)

    def wait(self, milliseconds: int):
        """
        Pause execution for a short time.
        """
        self.browser.page.wait_for_timeout(milliseconds)

    def wait_for_url(self, text: str, timeout: int = 10000):
        """
        Wait until the current URL contains the given text.
        """
        self.browser.page.wait_for_url(
            f"**{text}**",
            timeout=timeout
        )

    def get_text(self, selector: str):
        """
        Get text from an element.
        """
        locator = self.browser.page.locator(selector)
        return locator.inner_text()

    def screenshot(self, filename: str = "screenshot.png"):
        """
        Take a screenshot of the current page.
        """
        self.browser.page.screenshot(path=filename)

    def scroll_down(self, pixels: int = 800):
        """
        Scroll down the page.
        """
        self.browser.page.evaluate(
            f"window.scrollBy(0, {pixels})"
        )

    def scroll_up(self, pixels: int = 800):
        """
        Scroll up the page.
        """
        self.browser.page.evaluate(
            f"window.scrollBy(0, -{pixels})"
        )

    def current_title(self):
        """
        Return the title of the current page.
        """
        return self.browser.page.title()

    def current_url(self):
        """
        Return the current page URL.
        """
        return self.browser.page.url

    def exists(self, selector: str) -> bool:
        """
        Check whether an element exists.
        """
        return self.browser.page.locator(selector).count() > 0

    def is_visible(self, selector: str) -> bool:
        """
        Check whether an element is visible.
        """
        return self.browser.page.locator(selector).is_visible()

    def safe_click(self, selector: str, timeout: int = 5000):
        """
        Click an element if it becomes available.
        """
        try:
            self.wait_for(selector, timeout)
            self.click(selector)
            return True
        except TimeoutError:
            return False