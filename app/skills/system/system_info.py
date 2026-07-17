import psutil


class SystemInfo:
    """
    Provides live system information.
    """

    def battery(self):

        battery = psutil.sensors_battery()

        if battery is None:
            return None

        return {
            "percent": round(battery.percent),
            "charging": battery.power_plugged,
            "seconds_left": battery.secsleft,
        }

    def cpu(self):

        return {
            "usage": psutil.cpu_percent(interval=1),
        }

    def memory(self):

        memory = psutil.virtual_memory()

        return {
            "percent": memory.percent,
            "used": round(memory.used / (1024 ** 3), 2),
            "total": round(memory.total / (1024 ** 3), 2),
        }

    def disk(self):

        disk = psutil.disk_usage("/")

        return {
            "percent": disk.percent,
            "used": round(disk.used / (1024 ** 3), 2),
            "total": round(disk.total / (1024 ** 3), 2),
        }