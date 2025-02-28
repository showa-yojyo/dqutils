"""
Tests for dqutils.snescpu.disasm.
"""

from dqutils.dq3.disasm import DisassembleStateDQ3
from dqutils.snescpu.disasm import create_args


def test_create_args_default(rom):
    """Test create_args for DQ3 default values."""
    args, _ = create_args(rom, [])

    assert args["flags"] == 0
    assert args["first"] == 0xC00000
    assert args["last"] == -1
    assert not args["until_return"]


def test_specialized_state(fsm):
    """Test class `DisassembleStateDQ3`."""
    state = DisassembleStateDQ3(fsm)
    state.runtime_init()

    brk = state.get_instruction(0x00)
    assert brk.operand_size == 3

    cop = state.get_instruction(0x02)
    assert cop.operand_size == 1
