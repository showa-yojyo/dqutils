"""
Tests for disassembling DQ6.
"""

import re

import pytest

from .. import requires_config
from ..snescpu.test_statemachine import do_test_until_option

pytestmark = requires_config


def test_disassembled_code(fsm):
    """Test disassembled code for DQ6."""
    fsm.run(first=0xC2B09A, last=0xC2B13F)

    output_lines = fsm.destination.getvalue().split("\n")

    assert re.match(r"^C2/B09A:\s+6400\s+STZ \$00$", output_lines[0])
    assert re.match(r"^C2/B13E:\s+60\s+RTS$", output_lines[-2])
    assert output_lines[-1] == ""


def test_run_near_boundary_opcode_ca(fsm):
    """Test disassembling near boundary (opcode)."""
    fsm.run(first=0xCAFFFB, last=0xCB0000)

    output_lines = fsm.destination.getvalue().split("\n")

    assert re.match(r"^CA/FFFF:\s+FF$", output_lines[-2])
    assert output_lines[-1] == ""


def test_run_near_boundary_operand(fsm):
    """Test disassembling near boundary (operand)."""
    fsm.run(first=0xCBFFF5, last=0xCC0000)

    output_lines = fsm.destination.getvalue().split("\n")

    assert re.match(r"^CB/FFFD:\s+FFFFFF$", output_lines[-2])
    assert output_lines[-1] == ""


def test_run_near_boundary_opcode_ce(fsm):
    """Test disassembling near boundary (opcode)."""
    fsm.run(first=0xCEFFFD, until_return=True)

    output_lines = fsm.destination.getvalue().split("\n")

    assert re.match(r"^CE/FFFF:\s+6B\s+RTL$", output_lines[-2])
    assert output_lines[-1] == ""


@pytest.mark.parametrize(
    "offset,pattern",
    (
        (0xC2B091, r"^C2/B099:\s+60\s+RTS$"),
        (0xC2B4AF, r"^C2/B501:\s+6B\s+RTL$"),
    ),
)
def test_run_until_return(fsm, offset, pattern):
    """Test disassembling with -u option for the first return instruction occurrence."""
    do_test_until_option(fsm, offset, pattern)


def test_run_brk_operand(fsm):
    """Test if the operand of the BRK command is 2 bytes."""
    # The information booth in the Slime Arena.
    fsm.run(first=0xC3E601, until_return=True)

    output_lines = fsm.destination.getvalue().split("\n")

    for i in (
        0,
        5,
        12,
    ):
        line = output_lines[i]
        assert re.match(r"^C3/E6[0-9A-F]{2}:\s+00[0-9A-F]{2}07\s+", line)
        assert re.search(r"BRK #\$07[0-9A-F]{2}$", line)

    assert re.match(r"^C3/E62F:\s+6B\s+RTL$", output_lines[-2])
    assert output_lines[-1] == ""


def test_run_cop_operand(fsm):
    """Test if the COP command has no operands in DQ6."""
    fsm.run(first=0xCA0029, last=0xCA00AB)
    output_lines = fsm.destination.getvalue().split("\n")
    assert re.match(r"^CA/0029:\t02\s+COP$", output_lines[0])
    assert re.match(r"^CA/002A:\t4C1E00\s+JMP \$001E$", output_lines[1])


def test_jsr_args(fsm):
    """Test outputs of JSR instructions that have arguments."""
    # JSR $C92AB5 (RTL+8)
    fsm.run(first=0xC37D14, until_return=True)
    results = fsm.destination.getvalue().split("\n")

    hex_re = r"[0-9A-F]"

    assert results[0] == "C3/7D14:\t22B52AC9\tJSR $C92AB5"
    assert re.match("^C3/7D18:\t" + hex_re + "{2}$", results[1])
    assert re.match("^C3/7D19:\t" + hex_re + "{4}$", results[2])
    assert re.match("^C3/7D1B:\t" + hex_re + "{6}$", results[3])
    assert re.match("^C3/7D1E:\t" + hex_re + "{4}$", results[4])
    assert results[5] == "C3/7D20:\t8D8C38  \tSTA $388C"
