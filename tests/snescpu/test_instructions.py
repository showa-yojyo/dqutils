"""
Tests for dqutils.snescpu.instructions.
"""

import pytest

from dqutils.snescpu.instructions import INSTRUCTION_TABLE, get_instruction


@pytest.mark.parametrize("i,item", enumerate(INSTRUCTION_TABLE))
def test_get_instruction(i, item):
    """Test get_instruction."""
    inst = get_instruction(i)
    assert inst.opcode == i
    assert inst.mnemonic.upper()
    assert inst.mnemonic == item[0].upper()
    assert inst.operand_size == item[2]


@pytest.mark.parametrize("index", (666,))
def test_invalid_instruction(index, capture_stderr):
    """Test get_instruction for invalid opcode."""
    with pytest.raises(IndexError):
        get_instruction(index)
    assert not capture_stderr.getvalue()


def test_instruction_rep(fsm_mock):
    """Test REP."""
    inst = get_instruction(0xC2)
    assert inst.mnemonic == "REP"

    fsm_mock.flags, fsm_mock.current_operand = 0xFF, 0x30
    inst.execute(fsm_mock, None)
    assert fsm_mock.flags & 0x30 == 0

    fsm_mock.flags, fsm_mock.current_operand = 0xFF, 0x00
    inst.execute(fsm_mock, None)
    assert fsm_mock.flags == 0xFF


def test_instruction_sep(fsm_mock):
    """Test SEP."""
    inst = get_instruction(0xE2)
    assert inst.mnemonic == "SEP"

    fsm_mock.flags, fsm_mock.current_operand = 0xFF, 0x30
    inst.execute(fsm_mock, None)
    assert fsm_mock.flags == 0xFF

    fsm_mock.flags, fsm_mock.current_operand = 0x00, 0x30
    inst.execute(fsm_mock, None)
    assert fsm_mock.flags == 0x30


def test_wdm(fsm_mock):
    """Test WDM."""
    wdm = get_instruction(0x42)
    assert wdm.mnemonic == "WDM"

    flags = 0x11  # set arbitrary value
    fsm_mock.flags, fsm_mock.current_operand = flags, 0x22
    wdm.execute(fsm_mock, None)
    assert fsm_mock.flags == flags
