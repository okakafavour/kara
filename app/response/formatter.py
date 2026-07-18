from app.execution.models.action_result import ActionResult
from app.execution.models.result import ExecutionResult


class ResponseFormatter:
    """
    Converts execution results into natural,
    human-friendly responses.

    Supports both:

    • Legacy string messages
    • Structured ActionResult objects
    """

    SUCCESS = "✓"
    ERROR = "✗"
    INFO = "•"

    def format(self, results: list[ExecutionResult]) -> str:

        if not results:
            return "Done."

        lines = []

        success = 0
        failed = 0

        for result in results:

            if result.success:
                success += 1
            else:
                failed += 1

            lines.append(self._format_result(result))

        # -------------------------
        # Summary
        # -------------------------

        if len(results) > 1:

            summary = []

            if success:
                summary.append(f"{success} completed")

            if failed:
                summary.append(f"{failed} failed")

            if summary:
                lines.append("")
                lines.append(
                    f"{self.INFO} Summary: {', '.join(summary)}"
                )

        return "\n".join(lines)

    # -------------------------------------------------
    # Format one execution result
    # -------------------------------------------------

    def _format_result(
        self,
        result: ExecutionResult,
    ) -> str:

        message = result.message

        # Structured ActionResult
        if isinstance(message, ActionResult):
            return self._format_action(message)

        # Legacy string support
        if result.success:
            return str(message)

        return f"{self.ERROR} {message}"

    # -------------------------------------------------
    # Format ActionResult
    # -------------------------------------------------

    def _format_action(
        self,
        action: ActionResult,
    ) -> str:

        # -------------------------
        # Open Application
        # -------------------------

        if action.action == "open_application":

            app = action.payload.get(
                "application",
                "application",
            )

            if action.success:
                return f"{self.SUCCESS} Opened {app}."

            if action.error == "unknown_application":
                return (
                    f"{self.ERROR} "
                    f"I don't know how to open '{app}'."
                )

            if action.error == "not_installed":
                return (
                    f"{self.ERROR} "
                    f"{app.title()} is not installed."
                )

            if action.error:
                return (
                    f"{self.ERROR} "
                    f"Failed to open {app}: {action.error}"
                )

            return (
                f"{self.ERROR} "
                f"Couldn't open {app}."
            )

        # -------------------------
        # Browser
        # -------------------------

        elif action.action == "browser_open":

            url = action.payload.get("url", "")

            if action.success:
                return f"{self.SUCCESS} Opened {url}."

            return f"{self.ERROR} Couldn't open {url}."

        # -------------------------
        # Continue Project
        # -------------------------

        elif action.action == "continue_project":

            if not action.success:

                return action.payload.get(
                    "message",
                    "Couldn't continue the project.",
                )

            lines = [
                f"{self.SUCCESS} Switched to {action.payload['project']}.",
            ]

            if action.payload.get("backend"):
                lines.append(
                    f"Backend: {action.payload['backend']}"
                )

            if action.payload.get("frontend"):
                lines.append(
                    f"Frontend: {action.payload['frontend']}"
                )

            if action.payload.get("database"):
                lines.append(
                    f"Database: {action.payload['database']}"
                )

            if action.payload.get("branch"):
                lines.append(
                    f"Branch: {action.payload['branch']}"
                )

            if action.payload.get("workspace"):
                lines.append(
                    f"Workspace: {action.payload['workspace']}"
                )

            if action.payload.get("status"):
                lines.append(
                    f"Status: {action.payload['status']}"
                )

            if action.payload.get("last_task"):
                lines.append("")
                lines.append("Last task:")
                lines.append(action.payload["last_task"])

            if action.payload.get("next_task"):
                lines.append("")
                lines.append("Next task:")
                lines.append(action.payload["next_task"])

            return "\n".join(lines)

        # -------------------------
        # Battery
        # -------------------------

        elif action.action == "battery_status":

            level = action.payload.get("level")

            charging = (
                "charging"
                if action.payload.get(
                    "charging",
                    False,
                )
                else "not charging"
            )

            return (
                f"Battery is {level}% "
                f"and is {charging}."
            )

        # -------------------------
        # CPU
        # -------------------------

        elif action.action == "cpu_status":

            usage = action.payload.get("usage")

            return (
                f"CPU usage is {usage}%."
            )

        # -------------------------
        # Memory
        # -------------------------

        elif action.action == "memory_status":

            used = action.payload.get("used")
            total = action.payload.get("total")
            percent = action.payload.get("percent")

            return (
                f"Memory usage is "
                f"{used} GB of "
                f"{total} GB "
                f"({percent}%)."
            )

        # -------------------------
        # Disk
        # -------------------------

        elif action.action == "disk_status":

            used = action.payload.get("used")
            total = action.payload.get("total")
            percent = action.payload.get("percent")

            return (
                f"Disk usage is "
                f"{used} GB of "
                f"{total} GB "
                f"({percent}%)."
            )

        # -------------------------
        # Unknown Action
        # -------------------------

        return str(action.payload)