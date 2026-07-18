from app.session.manager import SessionManager


class ContextResolver:
    """
    Uses Kara's current session to resolve commands that
    depend on previous context.
    """

    def __init__(self, session: SessionManager):

        self.session = session

    def resolve(self, task: dict) -> dict:
        """
        Resolve a parsed task using the current session.

        The parser handles explicit commands.

        The ContextResolver handles commands whose meaning
        depends on previous actions or current state.
        """

        intent = task.get("intent")
        text = task.get("text", "").lower().strip()

        # -----------------------------------------
        # Rule 1
        # "go to github"
        # "go to youtube"
        # -----------------------------------------

        if intent == "unknown":

            if text.startswith("go to "):

                destination = text.removeprefix(
                    "go to "
                ).strip()

                if (
                    ".com" not in destination
                    and "." not in destination
                ):
                    destination += ".com"

                return {
                    "intent": "browser_open",
                    "entities": {
                        "url": f"https://{destination}"
                    },
                    "text": task.get("text", ""),
                }

        # -----------------------------------------
        # Rule 2
        # "continue working"
        # -----------------------------------------

        if intent == "unknown":

            if text in [
                "continue work",
                "continue working",
                "resume work",
                "resume workspace",
            ]:

                workspace = getattr(
                    self.session,
                    "current_workspace",
                    None,
                )

                if workspace:

                    return {
                        "intent": "start_workspace",
                        "entities": {
                            "workspace": workspace
                        },
                        "text": task.get("text", ""),
                    }

        # -----------------------------------------
        # Future rules go here
        # -----------------------------------------

        return task