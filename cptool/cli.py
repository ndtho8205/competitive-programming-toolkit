import argparse
from typing import Dict

from cptool import commands
from cptool.helpers import Env, errors
from cptool.version import VERSION


SUBCOMMANDS = {
    "new": commands.NewCommand(),
    "test": commands.TestCommand(),
    "testgen": commands.TestgenCommand(),
    "diff": commands.DiffCommand(),
}


def main():
    parser = _create_parser()
    args = parser.parse_args()

    if args.command in SUBCOMMANDS:
        env = Env()
        try:
            SUBCOMMANDS[args.command](env, args)
        except errors.Error as err:
            print(err.get_message())
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
