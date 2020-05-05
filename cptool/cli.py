import argparse
from typing import Dict

from cptool import commands
from cptool.utils import errors
from cptool.version import VERSION

SUBCOMMANDS = {
    "new": commands.NewCommand(),
    "scrap": commands.ScrapCommand(),
    "check": commands.CheckCommand(),
    "testgen": commands.TestgenCommand(),
    "test": commands.TestCommand(),
}


def main():
    parser = _create_parser()
    args = parser.parse_args()

    if args.command in SUBCOMMANDS:
        try:
            SUBCOMMANDS[args.command](args)
        except KeyboardInterrupt:
            aborted = errors.CptoolError("command aborted.")
            return aborted.get_message()
        except errors.Error as e:
            return e.get_message()
    else:
        # parser.print_help()
        raise errors.CptoolError("command {} not found.".format(args.command))


def _create_parser():
    parser = argparse.ArgumentParser(
        prog="cptool", description="A simple toolkit for Competitive Programming"
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
