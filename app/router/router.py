class DecisionRouter:
    """
    Decides whether a command should be handled
    by the Rule Engine or by the LLM.
    """

    def should_use_llm(self, command: str) -> bool:

        command = command.lower()

        simple_commands = [
            "open",
            "remember",
            "what is my",
            "what's my",
            "close",
            "exit",
            "quit",
        ]

        for phrase in simple_commands:
            if command.startswith(phrase):
                return False

        return True