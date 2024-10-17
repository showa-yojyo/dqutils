"""This is the dqutils (Dragon Quest Utilities) package.

This package contains the following sub-packages:

* dq3: Provides values and functions specific to DRAGONQUEST 3.
* dq5: Provides values and functions specific to DRAGONQUEST 5.
* dq6: Provides values and functions specific to DRAGONQUEST 6.
* database: Contains components for viewing structured data in ROM.

"""

from argparse import ArgumentParser
from collections import namedtuple
import sys

# Release data
from . import release

__author__ = '{} <{}>'.format(release.AUTHOR, release.AUTHOR_EMAIL)

__license__ = release.LICENSE

__date__ = release.DATE

__version__ = release.VERSION
"""major.minor.micro version number."""

Command = namedtuple('Command', ('name', 'help', 'func'))

def run(commands):
    """TBW.

    Under construction.

    Args:
      commands (iterable of Command): TBW

    Returns:
      None
    """

    parser = ArgumentParser(description='dqutils command line interface')
    parser.add_argument('--version', action='version', version=__version__)
    subparsers = parser.add_subparsers(help='commands')
    for i in commands:
        subp = subparsers.add_parser(i.name, help=i.help)
        subp.set_defaults(func=i.func)

    options = parser.parse_args(sys.argv[1:])
    options.func()
