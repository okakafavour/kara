from app.skills.base import BaseSkill
from app.skills.system.system_info import SystemInfo


class SystemSkill(BaseSkill):
    """
    Handles live system information.
    """

    def __init__(self):
        self.system = SystemInfo()

    @property
    def name(self):
        return "System"

    @property
    def description(self):
        return "Provides live system information."

    @property
    def intents(self):
        return [
            "battery_status",
            "cpu_status",
            "memory_status",
            "disk_status",
        ]

    def can_handle(self, task):

        return task.get("intent") in self.intents

    def execute(self, task):

        intent = task["intent"]

        if intent == "battery_status":

            battery = self.system.battery()

            if battery is None:
                return "Battery information is unavailable."

            status = (
                "charging"
                if battery["charging"]
                else "not charging"
            )

            return (
                f"Battery is currently "
                f"{battery['percent']}% "
                f"and is {status}."
            )

        if intent == "cpu_status":

            cpu = self.system.cpu()

            return (
                f"CPU usage is "
                f"{cpu['usage']}%."
            )

        if intent == "memory_status":

            memory = self.system.memory()

            return (
                f"Memory usage is "
                f"{memory['used']} GB "
                f"of {memory['total']} GB "
                f"({memory['percent']}%)."
            )

        if intent == "disk_status":

            disk = self.system.disk()

            return (
                f"Disk usage is "
                f"{disk['used']} GB "
                f"of {disk['total']} GB "
                f"({disk['percent']}%)."
            )

        return "Unknown system request."