"""
Tests for dqutils.snescpu.statemachine.
"""

import re

from .. import requires_config

pytestmark = requires_config


def test_disassembled_code(fsm):
    """Test disassembled code for DQ3."""
    fsm.run(first=0xC25BA6, last=0xC25BCE)

    output_lines = fsm.destination.getvalue().split("\n")
    assert re.match(r"^C2/5BA6:\s+A20000\s+LDX #\$0000$", output_lines[0])
    assert re.match(r"^C2/5BCD:\s+60\s+RTS$", output_lines[-2])
    assert output_lines[-1] == ""


def test_run_brk_operand(fsm):
    """Test if the operand of the BRK command is 2 bytes."""
    # People in the Shrine of Dharma.
    fsm.run(first=0xCB9A3E, last=0xCB9A57)

    output_lines = fsm.destination.getvalue().split("\n")

    for i in range(0, 8, 2):
        line = output_lines[i]
        assert re.match(r"^CB/[0-9A-F]{4}:\s+00[0-9A-F]{4}\s+", line)
        assert re.search(r"BRK #\$[0-9A-F]{4}$", line)

    assert re.match(r"^CB/9A56:\s+6B\s+RTL$", output_lines[-2])
    assert output_lines[-1] == ""


def test_run_cop_operand(fsm):
    """Test if the operand of the COP command varies."""
    fsm.run(first=0xCC001B, until_return=True)
    actual = fsm.destination.getvalue().partition("\n")
    expected = "CC/001B:	02      	COP"
    assert expected == actual[0]


def test_jsr_args(fsm):
    """Test outputs of JSR instructions that have arguments."""
    # JSR $C90572 (RTL+B)
    fsm.run(first=0xC66C1B, until_return=True)
    actual = fsm.destination.getvalue()
    expected = (
        "C6/6C1B:	227205C9	JSR $C90572\n"
        "C6/6C1F:	00\n"
        "C6/6C20:	0700\n"
        "C6/6C22:	B17DC8\n"
        "C6/6C25:	0000\n"
        "C6/6C27:	1F0000\n"
        "C6/6C2A:	997DA1  	STA $A17D,Y\n"
        ""
    )
    assert expected in actual
