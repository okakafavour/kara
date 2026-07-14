from app.skills.base import BaseSkill
from app.skills.browser.browser import BrowserEngine


class BrowserSkill(BaseSkill):
    """
    Skill responsible for browser automation.
    """

    def __init__(self):
        self.browser = BrowserEngine()

    @property
    def name(self) -> str:
        return "Browser"

    @property
    def description(self) -> str:
        return "Controls web browsers and automates web interactions."

    @property
    def intents(self) -> list[str]:
        return [
            "browser_open",
            "browser_search",
            "browser_close",
        ]

    def can_handle(self, task: dict) -> bool:
        return task.get("intent", "").startswith("browser")

    def execute(self, task: dict):

        intent = task.get("intent")

        entities = task.get("entities", {})

        if intent == "browser_open":

            url = entities.get("url")

            if not url:
                return "No URL was provided."
            
            self.browser.goto(url)

            return f"Opened {url}"

        elif intent == "browser_search":

            engine = entities.get("engine", "google")
            query = entities.get("query", "")

            if engine == "google":

                self.browser.goto("https://www.google.com")

                self.browser.actions.wait_for("textarea")

                self.browser.actions.type("textarea", query)

                self.browser.actions.press("textarea", "Enter")

                self.browser.actions.wait(3000)

                return f'Searched Google for "{query}"'

            return f"Search engine '{engine}' is not supported yet."

        elif intent == "browser_close":

            self.browser.close()

            return "Browser closed."

        return "Unknown browser command."