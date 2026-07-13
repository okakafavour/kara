import platform
import shutil
import subprocess
from typing import Dict


class DiscoveryEngine:
    """
    Responsible for discovering information
    about the computer Kara is running on.
    """

    def __init__(self):
        self.system_info = {}

    def discover(self) -> Dict:

        self.system_info = {
            "os": self.get_os(),
            "python": self.get_python(),
            "shell": self.get_shell(),
            "applications": self.get_applications(),
            "languages": self.get_languages(),
            "tools": self.get_tools(),
        }

        return self.system_info

    def get_os(self):

        return {
            "system": platform.system(),
            "release": platform.release(),
            "machine": platform.machine(),
        }

    def get_python(self):

        return platform.python_version()

    def get_shell(self):

        return subprocess.getoutput("echo $SHELL")

    def get_applications(self):

        apps = {
            "VS Code": "code",
            "Firefox": "firefox",
            "Google Chrome": "google-chrome",
            "Chromium": "chromium",
            "Terminal": "xfce4-terminal",
        }

        result = {}

        for name, executable in apps.items():
            result[name] = shutil.which(executable) is not None

        return result

    def get_languages(self):

        languages = {
            "Python": "python3",
            "Go": "go",
            "Java": "java",
            "Node": "node",
        }

        result = {}

        for name, executable in languages.items():
            result[name] = shutil.which(executable) is not None

        return result

    def get_tools(self):

        tools = {
            "Git": "git",
            "Docker": "docker",
            "Railway": "railway",
            "Flutter": "flutter",
        }

        result = {}

        for name, executable in tools.items():
            result[name] = shutil.which(executable) is not None

        return result