from rich.console import Console

from app.brain.brain import Brain
from app.context.context import ContextManager
from app.discovery.discovery import DiscoveryEngine
from app.execution.engine import ExecutionEngine
from app.planner.planner import Planner
from app.skills.manager import SkillManager

console = Console()


class KaraCore:
    """
    Main coordinator for the Kara AI Assistant.
    """

    def __init__(self):
        console.log("[bold green]Initializing Kara Core...[/bold green]")

        # Core Components
        self.brain = Brain()
        self.planner = Planner()
        self.skills = SkillManager()
        self.context = ContextManager()
        self.discovery = DiscoveryEngine()

        # Execution Engine
        self.execution = ExecutionEngine(
            skill_manager=self.skills,
            context=self.context,
        )

        # Discover current system
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
        """
        Start Kara's interactive command loop.
        """

        console.print("\n[bold magenta]Kara is ready![/bold magenta]\n")

        while True:

            command = input("kara > ").strip()

            if not command:
                continue

            if command.lower() in ("exit", "quit"):
                console.print("[yellow]Goodbye![/yellow]")
                break

            # Store conversation
            self.context.add_message(command)

            try:
                # Understand the command
                task = self.brain.process(command)

                # Remember the user's intent
                self.context.set_last_intent(task.get("intent"))

                # Create an execution plan
                plan = self.planner.create_plan(task)

                console.print(
                    f"\n[cyan]Goal:[/cyan] {plan.goal}"
                )

                # Execute the plan
                results = self.execution.execute(plan)

                # Display results
                for result in results:

                    if result.success:
                        console.print(
                            f"[green]✓ {result.message}[/green]"
                        )
                    else:
                        console.print(
                            f"[bold red]✗ {result.message}[/bold red]"
                        )

                # Mark plan complete
                plan.completed = True

            except Exception as error:
                console.print(
                    f"[bold red]Error:[/bold red] {error}"
                )