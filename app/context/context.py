from app.context.models import ContextModel


class ContextManager:
    """
    Stores Kara's short-term memory for the current session.
    """

    def __init__(self):
        self.context = ContextModel()

    # ---------- Conversation ----------

    def add_message(self, message: str):
        self.context.conversation.append(message)

        # Keep only the last 20 messages
        self.context.conversation = self.context.conversation[-20:]

    def get_conversation(self):
        return self.context.conversation

    # ---------- Current State ----------

    def set_application(self, application: str):
        self.context.current_application = application

    def get_application(self):
        return self.context.current_application

    def set_website(self, website: str):
        self.context.current_website = website

    def get_website(self):
        return self.context.current_website

    # ---------- Intent ----------

    def set_last_intent(self, intent: str):
        self.context.last_intent = intent

    def get_last_intent(self):
        return self.context.last_intent

    # ---------- Tool ----------

    def set_last_tool(self, tool: str):
        self.context.last_tool = tool

    def get_last_tool(self):
        return self.context.last_tool

    # ---------- Working Memory ----------

    def remember(self, key: str, value):
        self.context.working_memory[key] = value

    def recall(self, key: str):
        return self.context.working_memory.get(key)

    def clear_working_memory(self):
        self.context.working_memory.clear()