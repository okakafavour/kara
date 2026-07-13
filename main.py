from rich.console import Console

from app.core.core import KaraCore

console = Console()


def main():
    console.print("""
[bold cyan]
╔══════════════════════════════════════╗
║          KARA AI ASSISTANT           ║
╚══════════════════════════════════════╝
[/bold cyan]
""")

    kara = KaraCore()
    kara.start()


if __name__ == "__main__":
    main()