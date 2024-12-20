"""This is the dqutils (Dragon Quest Utilities) dq5 subpackage."""

from dqutils import Command, run
from dqutils.dq5.message import print_all_battle, print_all_scenario
from dqutils.dq5.string import print_all


def main():
    """See :code:`python -m dqutils.dq5 --help`."""

    commands = (
        Command(name="print-scenario-messages", help="print messages", func=print_all_scenario),
        Command(name="print-battle-messages", help="print messages", func=print_all_battle),
        Command(name="print-strings", help="print strings", func=print_all),
    )

    return run(commands)


if __name__ == "__main__":
    main()
