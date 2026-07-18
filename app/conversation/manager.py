from app.conversation.models import PendingAction
from app.conversation.replies import NO_REPLIES, YES_REPLIES
from app.conversation.state import ConversationState


class ConversationManager:
    """
    Handles conversations that span
    multiple user messages.
    """

    def __init__(self):

        self.state = ConversationState()

    # --------------------------------------------------
    # State
    # --------------------------------------------------

    def waiting(self) -> bool:
        """
        Returns True if Kara is waiting
        for a user response.
        """

        return self.state.waiting

    def pending(self):
        """
        Returns the current pending action.
        """

        return self.state.pending_action

    # --------------------------------------------------
    # Conversation Control
    # --------------------------------------------------

    def ask_confirmation(
        self,
        plan,
        question,
        action="confirmation",
    ):
        """
        Store a pending action that requires
        user confirmation.
        """

        self.state.pending_action = PendingAction(
            plan=plan,
            question=question,
            action=action,
        )

        return question

    def resume(self):
        """
        Return the pending action without
        clearing it.
        """

        return self.state.pending_action

    def confirm(self):
        """
        User accepted the pending action.

        Returns the stored execution plan and
        clears the conversation state.
        """

        if not self.waiting():
            return None

        plan = self.state.pending_action.plan

        self.clear()

        return plan

    def reject(self):
        """
        User rejected the pending action.

        Clears the conversation state.
        """

        self.clear()

        return "Okay, cancelled."

    def clear(self):
        """
        Clear the current conversation state.
        """

        self.state.clear()

    # --------------------------------------------------
    # Reply Detection
    # --------------------------------------------------

    def is_reply(self, text: str) -> bool:
        """
        Check whether the user's message is
        a reply to the pending conversation.
        """

        if not self.waiting():
            return False

        text = text.lower().strip()

        return (
            text in YES_REPLIES
            or text in NO_REPLIES
        )

    def resolve_reply(self, text: str):
        """
        Resolve the user's reply into a
        standardized response.
        """

        text = text.lower().strip()

        if text in YES_REPLIES:
            return "yes"

        if text in NO_REPLIES:
            return "no"

        return None