"""
Tests for dqutils.snescpu.statemachine.
"""

import re

import pytest

from dqutils.dq5.disasm import DisassembleStateDQ5, DumpState
from dqutils.snescpu.rom_image import RomImage

from ..snescpu.test_statemachine import do_test_initial, do_test_until_option

GAME_TITLE = "DRAGONQUEST5"
STATE_CLASSES = (DisassembleStateDQ5, DumpState)
INITIAL_STATE = "DisassembleStateDQ5"


@pytest.fixture
def state_classes():
    return STATE_CLASSES


@pytest.fixture
def initial_state():
    return INITIAL_STATE


@pytest.fixture
def rom():
    with RomImage(GAME_TITLE) as retval:
        yield retval


def test_initial(fsm):
    """Test the initial condition of StateMachine for DQ5."""
    do_test_initial(fsm)


def test_disassembled_code(fsm):
    """Test disassembled code for DQ5."""
    fsm.run(first=0x23E1FE, last=0x23E24C)

    output_lines = fsm.destination.getvalue().split("\n")

    assert re.match(r"^23/E1FE:\s+08\s+PHP$", output_lines[0])
    assert re.match(r"^23/E24B:\s+6B\s+RTL$", output_lines[-2])
    assert output_lines[-1] == ""


def test_run_until_return(fsm):
    """Test disassembling with -u option for the first return
    instruction occurrence.
    """

    do_test_until_option(fsm, 0x008F80, r"^00/8FAB:\s+40\s+RTI$")


def _do_test_brk(fsm, expected, **kwargs):
    fsm.run(**kwargs)
    actual = fsm.destination.getvalue()
    assert expected == actual


def test_disassemble_brk_00(fsm):
    """Test `BRK #$00`."""
    expected = (
        "00/B1ED:	0000    	BRK #$00\n"
        "00/B1EF:	B705    	LDA [$05],Y\n"
        "00/B1F1:	2904    	AND #$04\n"
    )
    _do_test_brk(fsm, expected, first=0x00B1ED, last=0x00B1F3, flags=0x20)


def test_disassemble_brk_01(fsm):
    """Test `BRK #$01`."""
    # fmt: off
    expected = (
        "00/A717:	0001    	BRK #$01\n"
        "00/A719:	0018    	BRK #$18\n"
        "00/A71B:	101E\n"
    )
    # fmt: on
    _do_test_brk(fsm, expected, first=0x00A717, last=0x00A71D)


def test_disassemble_brk_02(fsm):
    """Test `BRK #$02`."""
    # fmt: off
    expected = (
        "00/9808:	0002    	BRK #$02\n"
        "00/980A:	C230    	REP #$30\n"
    )
    # fmt: on
    _do_test_brk(fsm, expected, first=0x009808, last=0x00980C)


def test_disassemble_brk_03(fsm):
    """Test `BRK #$03`."""
    # fmt: off
    expected = (
        "00/97FE:	0003    	BRK #$03\n"
        "00/9800:	6B      	RTL\n"
    )
    # fmt: on
    _do_test_brk(fsm, expected, first=0x0097FE, last=0x009801)


def test_disassemble_brk_04(fsm):
    """Test `BRK #$04`."""
    # fmt: off
    expected = (
        "01/DDD0:	0004    	BRK #$04\n"
        "01/DDD2:	3CB4\n"
    )
    # fmt: on
    _do_test_brk(fsm, expected, first=0x01DDD0, last=0x01DDD4)


def test_disassemble_brk_06(fsm):
    """Test `BRK #$06`."""
    # fmt: off
    expected = (
        "20/BD91:	0006    	BRK #$06\n"
        "20/BD93:	A905    	LDA #$05\n"
    )
    # fmt: on
    _do_test_brk(fsm, expected, first=0x20BD91, last=0x20BD95, flags=0x20)


def test_disassemble_brk_08(fsm):
    """Test `BRK #$08`."""
    # fmt: off
    expected = (
        "00/816A:	0008    	BRK #$08\n"
        "00/816C:	CA      	DEX\n"
    )
    # fmt: on
    _do_test_brk(fsm, expected, first=0x00816A, last=0x00816D)


def test_disassemble_brk_09(fsm):
    """Test `BRK #$09`."""
    # fmt: off
    expected = (
        "00/C0AE:	0009    	BRK #$09\n"
        "00/C0B0:	10\n"
    )
    # fmt: on
    _do_test_brk(fsm, expected, first=0x00C0AE, last=0x00C0B1)


def test_disassemble_brk_0b(fsm):
    """Test `BRK #$0B` and `BRK #$0C`."""
    expected = (
        "00/A732:	000B    	BRK #$0B\n"
        "00/A734:	4000\n"
        "00/A736:	D009    	BNE $A741\n"
        "00/A738:	000C    	BRK #$0C\n"
        "00/A73A:	0200\n"
    )
    _do_test_brk(fsm, expected, first=0x00A732, last=0x00A73C)


def test_disassemble_brk_0d(fsm):
    """Test `BRK #$0D`."""
    expected = (
        "00/A8F8:	000D    	BRK #$0D\n"
        "00/A8FA:	7F15\n"
        "00/A8FC:	000B    	BRK #$0B\n"
        "00/A8FE:	0126\n"
    )
    _do_test_brk(fsm, expected, first=0x00A8F8, last=0x00A900)


def test_disassemble_brk_0e(fsm):
    """Test `BRK #$0E`."""
    # fmt: off
    expected = (
        "00/BF91:	000E    	BRK #$0E\n"
        "00/BF93:	0095    	BRK #$95\n"
        "00/BF95:	FF\n")
    # fmt: on
    _do_test_brk(fsm, expected, first=0x00BF91, last=0x00BF96)


def test_disassemble_brk_12(fsm):
    """Test `BRK #$12`."""
    expected = (
        "00/CA33:	0012    	BRK #$12\n"
        "00/CA35:	44\n"
        "00/CA36:	0012    	BRK #$12\n"
        "00/CA38:	44\n"
    )
    _do_test_brk(fsm, expected, first=0x00CA33, last=0x00CA39)


def test_disassemble_brk_19(fsm):
    """Test `BRK #$19`."""
    # fmt: off
    expected = (
        "00/8110:	0019    	BRK #$19\n"
        "00/8112:	3300\n")
    # fmt: on
    _do_test_brk(fsm, expected, first=0x008110, last=0x008114)


def test_disassemble_brk_95(fsm):
    """Test `BRK #$95` and `BRK #$99`."""
    # fmt: off
    expected = (
        "00/C46C:	0095    	BRK #$95\n"
        "00/C46E:	00\n"
        "00/C46F:	0099    	BRK #$99\n"
        "00/C471:	AA\n"
    )
    # fmt: on
    _do_test_brk(fsm, expected, first=0x00C46C, last=0x00C472)


def test_disassemble_brk_9c(fsm):
    """Test `BRK #$9C`."""
    # fmt: off
    expected = (
        "00/C40C:	009C    	BRK #$9C\n"
        "00/C40E:	80\n"
    )
    # fmt: on
    _do_test_brk(fsm, expected, first=0x00C40C, last=0x00C40F)


@pytest.mark.skip(reason="no way of currently testing this")
def test_disassemble_cop_operand(fsm):
    """Test if the operand of the COP command varies."""
    pytest.xfail("DQ5 COP")
