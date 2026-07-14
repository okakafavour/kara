class TaskNormalizer:
    """
    Converts every parser output into Kara's
    standard internal task format.
    """

    FIELD_MAPPING = {
        "target": "application",
    }

    @classmethod
    def normalize(cls, task: dict) -> dict:
        """
        Normalize any task into:

        {
            "intent": "...",
            "entities": {...}
        }
        """

        if not task:
            return {
                "intent": "unknown",
                "entities": {}
            }

        intent = task.get("intent", "unknown")

        entities = task.get("entities")

        if entities is None:
            entities = {}

            for key, value in task.items():

                if key == "intent":
                    continue

                canonical = cls.FIELD_MAPPING.get(key, key)

                entities[canonical] = value

        return {
            "intent": intent,
            "entities": entities
        }