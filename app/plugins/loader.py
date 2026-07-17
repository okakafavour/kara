import importlib
import inspect
import pkgutil


class PluginLoader:
    """
    Generic plugin loader used throughout Kara.

    It automatically discovers subclasses of a given
    base class inside a package (and its sub-packages).
    """

    @staticmethod
    def load(package_name: str, base_class):

        plugins = []

        package = importlib.import_module(package_name)

        # Walk through every module and sub-package
        for _, module_name, is_package in pkgutil.walk_packages(
            package.__path__,
            package.__name__ + ".",
        ):

            # Skip __init__.py modules
            if module_name.endswith("__init__"):
                continue

            # Skip abstract base classes
            if module_name.endswith(".base"):
                continue

            module = importlib.import_module(module_name)

            for _, obj in inspect.getmembers(module, inspect.isclass):

                if (
                    issubclass(obj, base_class)
                    and obj is not base_class
                    and obj.__module__ == module.__name__
                ):
                    plugins.append(obj())

        return plugins