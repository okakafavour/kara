from app.memory.models import MemoryModel


class Memory:

    def __init__(self):
        self.model = MemoryModel()

    def remember(self, key: str, value: str):
        self.model.save(key, value)

    def recall(self, key: str):
        return self.model.get(key)

    def forget(self, key: str):
        self.model.delete(key)

    def all(self):
        return self.model.get_all()