"""
Tests for dqutils.snescpu.instructions.
"""

from unittest.mock import Mock

import pytest

from dqutils.snescpu.instructions import INSTRUCTION_TABLE, get_instruction


def test_get_instruction():
    """Test get_instruction."""
    for i, item in enumerate(INSTRUCTION_TABLE):
        inst = get_instruction(i)
        assert inst.opcode == i
        assert inst.mnemonic.upper()
        assert inst.mnemonic == item[0].upper()
        assert inst.operand_size == item[2]


def test_invalid_instruction():
    """Test get_instruction for invalid opcode."""
    with pytest.raises(IndexError):
        get_instruction(666)


def test_instruction_rep():
    """Test REP."""
    inst = get_instruction(0xC2)
    assert inst.mnemonic == "REP"

    fsm = Mock(flags=0xFF, current_operand=0x30)
    inst.execute(fsm, None)
    assert fsm.flags & 0x30 == 0

    fsm = Mock(flags=0xFF, current_operand=0x00)
    inst.execute(fsm, None)
    assert fsm.flags == 0xFF


def test_instruction_sep():
    """Test SEP."""
    inst = get_instruction(0xE2)
    assert inst.mnemonic == "SEP"

    fsm = Mock(flags=0xFF, current_operand=0x30)
    inst.execute(fsm, None)
    assert fsm.flags == 0xFF

    fsm = Mock(flags=0x00, current_operand=0x30)
    inst.execute(fsm, None)
    assert fsm.flags == 0x30


def test_wdm():
    """Test WDM."""
    wdm = get_instruction(0x42)
    assert wdm.mnemonic == "WDM"

    flags, operand = 0x11, 0x22  # set arbitrary value
    fsm = Mock(flags=flags, current_operand=operand)
    wdm.execute(fsm, None)
    assert fsm.flags == flags
