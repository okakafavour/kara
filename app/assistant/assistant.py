from app.brain.rule_parser import RuleParser
from app.context.context import ContextManager
from app.context.resolver import ContextResolver
from app.conversation.manager import ConversationManager
from app.decision.engine import DecisionEngine
from app.execution.engine import ExecutionEngine
from app.planner.planner import Planner
from app.response.formatter import ResponseFormatter
from app.session.manager import SessionManager
from app.skills.manager import SkillManager


class KaraAssistant:
    """
    Kara's main entry point.

    Coordinates every subsystem:

    - Rule Parser
    - Context Resolver
    - Planner
    - Decision Engine
    - Conversation Manager
    - Execution Engine
    - Session Manager
    - Skill Manager
    - Response Formatter
    """

    def __init__(self):

        # -----------------------------
        # Core Components
        # -----------------------------

        self.parser = RuleParser()
        self.planner = Planner()

        # -----------------------------
        # State
        # -----------------------------

        self.context = ContextManager()
        self.session = SessionManager()
        self.conversation = ConversationManager()

        # -----------------------------
        # Context Resolver
        # -----------------------------

        self.context_resolver = ContextResolver(
            self.session
        )

        # -----------------------------
        # Skills
        # -----------------------------

        self.skill_manager = SkillManager()

        # -----------------------------
        # Response Formatter
        # -----------------------------

        self.formatter = ResponseFormatter()

        # -----------------------------
        # Engines
        # -----------------------------

        self.decision_engine = DecisionEngine()

        self.execution_engine = ExecutionEngine(
            skill_manager=self.skill_manager,
            context=self.context,
            session=self.session,
        )

    def process(self, command: str):
        """
        Process a user message.
        """

        command = command.strip()

        # =====================================
        # Handle replies to previous questions
        # =====================================

        if self.conversation.is_reply(command):

            reply = self.conversation.resolve_reply(command)

            if reply == "yes":

                plan = self.conversation.confirm()

                if plan is None:
                    return "There is nothing to continue."

                results = self.execution_engine.execute(plan)

                return self.formatter.format(results)

            if reply == "no":

                return self.conversation.reject()

        # =====================================
        # Parse command
        # =====================================

        task = self.parser.parse(command)

        # =====================================
        # Resolve context
        # =====================================

        task = self.context_resolver.resolve(task)

        # =====================================
        # Unknown command
        # =====================================

        if task["intent"] == "unknown":
            return "Sorry, I don't understand that yet."

        # =====================================
        # Create execution plan
        # =====================================

        plan = self.planner.create_plan(task)

        # =====================================
        # Evaluate the plan
        # =====================================

        decision = self.decision_engine.evaluate(
            plan,
            self.session,
        )

        if not decision.proceed:

            if decision.requires_confirmation:

                return self.conversation.ask_confirmation(
                    plan=plan,
                    question=decision.question,
                )

            return decision.question

        # =====================================
        # Execute the approved plan
        # =====================================

        results = self.execution_engine.execute(plan)

        return self.formatter.format(results)