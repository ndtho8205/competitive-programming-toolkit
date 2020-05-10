import sys

from .cli import main
from .version import VERSION

__version__ = VERSION


def run_main():
    sys.exit(main())


if __name__ == "__main__":
    run_main()
