import platform
import time
from os.path import abspath, dirname

project_path = dirname(dirname(abspath(__file__)))


class Tool:
    def __init__(self, driver=None, json_data=None):
        self.WebTool_driver = driver
        self.json_data = json_data
        self.start_timestamp = self.get_timestamp()
        self.end_timestamp = self.get_timestamp()
        self.last_step = ""

    @staticmethod
    def is_running_on_windows():
        return platform.system() == "Windows"

    def get_current_datetime(self):
        from datetime import datetime
        current_time = datetime.now()
        current_datetime = current_time.strftime("%Y-%m-%d %H:%M:%S")
        return current_datetime

    def get_timestamp(self):
        timestamp = time.time_ns() // 1_000_000
        return timestamp
