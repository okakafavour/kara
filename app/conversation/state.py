from app.conversation.models import PendingAction


class ConversationState:
    """
    Stores the current conversation state.
    """

    def __init__(self):

        self.pending_action: PendingAction | None = None

    @property
    def waiting(self) -> bool:

        return self.pending_action is not None

    def clear(self):

        self.pending_action = None