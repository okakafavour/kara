from rich.console import Console

from app.brain.brain import Brain
from app.discovery.discovery import DiscoveryEngine
from app.tools.tool_manager import ToolManager

console = Console()


class KaraCore:
    """Main coordinator for the Kara AI Assistant."""

    def __init__(self):
        console.log("[bold green]Initializing Kara Core...[/bold green]")

        # Initialize core components
        self.brain = Brain()
        self.tools = ToolManager()
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

            if not command:
                continue

            if command.lower() in ("exit", "quit"):
                console.print("[yellow]Goodbye![/yellow]")
                break

            try:
                task = self.brain.process(command)
                response = self.tools.execute(task)

                console.print(f"[green]{response}[/green]")

            except Exception as error:
                console.print(f"[bold red]Error:[/bold red] {error}")