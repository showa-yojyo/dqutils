"""
Helper testing functions for tests.dq{3,5,6}.test_statemachine.
"""

import re


def do_test_initial(fsm):
    """Test the initial condition of an object of StateMachine."""
    assert fsm.program_counter in (0x008000, 0xC00000)
    assert fsm.mapper is not None


def do_test_until_option(fsm, first, pattern):
    """This method is used from `test_with_until_option`."""
    fsm.run(first=first, until_return=True)

    output_lines = fsm.destination.getvalue().split("\n")

    for line in output_lines[:-2]:
        assert not re.match(r"(RTI|RTS|RTL)", line)

    assert re.match(pattern, output_lines[-2])
    assert output_lines[-1] == ""
