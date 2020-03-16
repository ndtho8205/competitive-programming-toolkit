# import sys
# sys.tracebacklimit = 0

import argparse
from typing import Dict

from cptool.version import VERSION
from cptool.commands import NewCommand, TestCommand, TestgenCommand, DiffCommand

SUBCOMMANDS = {
    "new": NewCommand(),
    "test": TestCommand(),
    "testgen": TestgenCommand(),
    "diff": DiffCommand(),
}


def main():
    parser = _create_parser()
    args = parser.parse_args()

    if args.command in SUBCOMMANDS:
        SUBCOMMANDS[args.command](args)
    else:
        parser.print_help()


def _create_parser():
    parser = argparse.ArgumentParser(
        prog="cptool", description="A toolkit for Competitive Programming"
    )

    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"%(prog)s {VERSION}",
        help="print version info",
    )

    _add_subcommand(parser, SUBCOMMANDS)

    return parser


def _add_subcommand(parser, subcommands: Dict):
    subparsers = parser.add_subparsers(metavar="[SUBCOMMAND]", dest="command")

    for title, subcommand in subcommands.items():
        parser = subparsers.add_parser(
            title, description=subcommand.__doc__, help=subcommand.__doc__
        )
        subcommand.register_arguments(parser)
