import psutil

from app.events.base import BaseEventSource
from app.events.event import Event


class BatterySource(BaseEventSource):
    """
    Monitors the system battery.
    """

    def __init__(self):

        self.previous_low = False
        self.previous_charging = None

    @property
    def name(self):

        return "Battery"

    def poll(self):

        battery = psutil.sensors_battery()

        # Desktop PC or battery unavailable
        if battery is None:
            return None

        level = round(battery.percent)

        charging = battery.power_plugged

        # -----------------------------
        # Low battery detected
        # -----------------------------

        if level <= 20 and not charging:

            if not self.previous_low:

                self.previous_low = True

                return Event(
                    source="battery",
                    intent="battery_low",
                    entities={
                        "level": level,
                    },
                )

        else:

            self.previous_low = False

        # -----------------------------
        # Charging state changed
        # -----------------------------

        if self.previous_charging is None:

            self.previous_charging = charging

            return None

        if charging != self.previous_charging:

            self.previous_charging = charging

            return Event(
                source="battery",
                intent=(
                    "battery_charging"
                    if charging
                    else "battery_unplugged"
                ),
                entities={
                    "level": level,
                },
            )

        return None