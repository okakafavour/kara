import subprocess

from rich.console import Console

console = Console()


class ApplicationTool:

    APPS = {
        "vscode": "code",
        "code": "code",
        "firefox": "firefox",
        "terminal": "gnome-terminal",
        "files": "xdg-open ~",
        "file manager": "xdg-open ~",
    }

    def open(self, target: str):

        command = self.APPS.get(target)

        if command is None:
            return f"I don't know how to open '{target}'."

        try:
            subprocess.Popen(command, shell=True)
            return f"Opening {target}..."
        except Exception as e:
            return str(e)