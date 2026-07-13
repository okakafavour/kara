from rich.console import Console

from app.brain.brain import Brain
from app.context.context import ContextManager
from app.discovery.discovery import DiscoveryEngine
from app.planner.planner import Planner
from app.tools.tool_manager import ToolManager

console = Console()


class KaraCore:
    """Main coordinator for the Kara AI Assistant."""

    def __init__(self):
        console.log("[bold green]Initializing Kara Core...[/bold green]")

        # Core components
        self.brain = Brain()
        self.planner = Planner()
        self.tools = ToolManager()
        self.context = ContextManager()
        self.discovery = DiscoveryEngine()

        # Discover the current system
        console.log("[yellow]Scanning system...[/yellow]")

        try:
            self.system = self.discovery.discover()

            console.log("[green]System scan complete[/green]")

            console.print("\n[bold cyan]System Information[/bold cyan]")
            console.print(self.system)

        except Exception as error:
            console.log(f"[bold red]Discovery failed:[/bold red] {error}")
            self.system = {}

        console.log("[bold blue]Kara Core Ready[/bold blue]")

    def start(self):
        """Start Kara's interactive command loop."""

        console.print("\n[bold magenta]Kara is ready![/bold magenta]\n")

        while True:
            command = input("kara > ").strip()

            # Ignore empty commands
            if not command:
                continue

            # Store conversation
            self.context.add_message(command)

            # Exit
            if command.lower() in ("exit", "quit"):
                console.print("[yellow]Goodbye![/yellow]")
                break

            try:
                # Understand the command
                task = self.brain.process(command)

                self.context.set_last_intent(task.get("intent"))

                # Create execution plan
                plan = self.planner.create_plan(task)

                # Execute the plan
                for step in plan:

                    intent = step.get("intent")

                    self.context.set_last_tool(intent)

                    # Remember active application
                    if intent == "open_application":
                        self.context.set_application(step.get("target"))

                    response = self.tools.execute(step)

                    console.print(f"[green]{response}[/green]")

            except Exception as error:
                console.print(f"[bold red]Error:[/bold red] {error}")