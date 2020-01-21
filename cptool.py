#!/usr/bin/env python

__version__ = "0.1.0"

# import sys
import argparse

from src import config, create, testgen, test

# sys.tracebacklimit = 0

parser = argparse.ArgumentParser(
    prog="cptool", description="A toolkit for Competitive Programming"
)
parser.add_argument(
    "--create",
    metavar="PROBLEM_NAME",
    help="create a new problem from a sample template",
    type=str,
)
parser.add_argument(
    "--testgen",
    metavar="NUMBER_OF_TEST_CASE",
    help="generate a number of test cases based on your logic/logic.py",
    type=int,
)
parser.add_argument(
    "--test", help="test your codes on test cases", action="store_true", default=False
)
parser.add_argument(
    "--diff",
    help="show different between *.ans files",
    metavar="FILES",
    type=str,
    nargs="+",
)

if __name__ == "__main__":
    args = parser.parse_args()

    if args.create:
        create.create(config.CURRENT_PATH, args.create)
    elif args.testgen:
        testgen.generate(config.CURRENT_PATH, args.testgen)
    elif args.test:
        test.test(config.CURRENT_PATH)
