import json
from pathlib import Path


class ProfileStorage:
    """
    Loads browser profiles and workspaces from disk.
    """

    def __init__(self):

        self.file = (
            Path(__file__).parent / "profiles.json"
        )

    def load(self):

        with open(
            self.file,
            "r",
            encoding="utf-8",
        ) as f:

            return json.load(f)