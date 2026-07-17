import importlib
import inspect
import pkgutil

from rich.console import Console

from app.events.base import BaseEventSource

console = Console()


class EventManager:
    """
    Automatically discovers and manages every event source.
    """

    def __init__(self):

        self.sources = []

        self.load_sources()

    def load_sources(self):
        """
        Discover every installed event source.
        """

        package = importlib.import_module(
            "app.events.sources"
        )

        for _, module_name, _ in pkgutil.iter_modules(
            package.__path__
        ):

            if module_name.startswith("__"):
                continue

            module = importlib.import_module(
                f"app.events.sources.{module_name}"
            )

            for _, obj in inspect.getmembers(
                module,
                inspect.isclass,
            ):

                if (
                    issubclass(obj, BaseEventSource)
                    and obj is not BaseEventSource
                ):

                    source = obj()

                    console.log(
                        f"[green]Loaded Event Source:[/green] {source.name}"
                    )

                    self.sources.append(source)

    def poll(self):
        """
        Poll every event source and collect any new events.
        """

        events = []

        for source in self.sources:

            try:

                event = source.poll()

                if event is not None:
                    events.append(event)

            except Exception as error:

                console.log(
                    f"[bold red]Event Source Failed:[/bold red] "
                    f"{source.name}: {error}"
                )

        return events