# -*- coding: utf-8 -*-
"""This is the dqutils (Dragon Quest Utilities) dq3 sub-package.

It contains a few modules for access to data stored in ROM of DRAGONQUEST 3.
"""

from dqutils import Command
from dqutils import run
from dqutils.dq3.message import print_all_battle
from dqutils.dq3.message import print_all_scenario
from dqutils.dq3.string import print_all

def main():
    """dqutils.dq3.main function.

    It deligates `dqutils.run()`.

    Returns:
      None
    """

    commands = (
        Command(
            name='print-scenario-messages',
            help='print messages',
            func=print_all_scenario),
        Command(
            name='print-battle-messages',
            help='print messages',
            func=print_all_battle),
        Command(
             name='print-strings',
             help='print strings',
             func=print_all),)

    return run(commands)

if __name__ == '__main__':
    main()
