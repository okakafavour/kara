from app.conversation.models import PendingAction
from app.conversation.state import ConversationState


class ConversationManager:
    """
    Handles conversations that span
    multiple user messages.
    """

    def __init__(self):

        self.state = ConversationState()

    # ------------------------

    def waiting(self):

        return self.state.waiting

    # ------------------------

    def pending(self):

        return self.state.pending_action

    # ------------------------

    def ask_confirmation(
        self,
        plan,
        question,
        action="confirmation",
    ):

        self.state.pending_action = PendingAction(
            plan=plan,
            question=question,
            action=action,
        )

        return question

    # ------------------------

    def clear(self):

        self.state.clear()