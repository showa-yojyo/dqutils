"""This is the dqutils (Dragon Quest Utilities) package.

This package contains the following sub-packages:

* dq3: Provides values and functions specific to DRAGONQUEST 3.
* dq5: Provides values and functions specific to DRAGONQUEST 5.
* dq6: Provides values and functions specific to DRAGONQUEST 6.
* database: Contains components for viewing structured data in ROM.

"""

import sys
from argparse import ArgumentParser
from collections.abc import Callable, Iterable
from typing import NamedTuple

# Release data
from dqutils.release import __version__


class Command(NamedTuple):
    name: str
    help: str
    func: Callable


def run(commands: Iterable[Command]) -> None:
    """TBW.

    Under construction.

    Args:
      commands (iterable of Command): TBW

    Returns:
      None
    """

    parser = ArgumentParser(description="dqutils command line interface")
    parser.add_argument("--version", action="version", version=__version__)
    subparsers = parser.add_subparsers(help="commands")
    for i in commands:
        subp = subparsers.add_parser(i.name, help=i.help)
        subp.set_defaults(func=i.func)

    options = parser.parse_args(sys.argv[1:])
    options.func()
