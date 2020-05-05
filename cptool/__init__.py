from cptool import version
from cptool.cptool import Cptool

from .cli import main

__version__ = version.VERSION
del version

__all__ = ["__version__", "main", "Cptool"]
