"""This is the dqutils (Dragon Quest Utilities) dq3 subpackage."""

from dqutils import Command, run
from dqutils.dq3.message import print_all_battle, print_all_scenario
from dqutils.dq3.string import print_all


def main() -> None:
    """See :code:`python -m dqutils.dq3 --help`."""

    commands = (
        Command(name="print-scenario-messages", help="print messages", func=print_all_scenario),
        Command(name="print-battle-messages", help="print messages", func=print_all_battle),
        Command(name="print-strings", help="print strings", func=print_all),
    )

    run(commands)


if __name__ == "__main__":
    main()
