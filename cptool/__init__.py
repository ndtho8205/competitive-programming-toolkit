from .cli import main

from cptool import version

__version__ = version.VERSION
del version

__all__ = ["__version__", "main"]
