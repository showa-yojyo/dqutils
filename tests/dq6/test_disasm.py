"""Tests dqutils.snescpu.disasm for DQ6."""

import pytest

from dqutils.dq6.disasm import DisassembleStateDQ6
from dqutils.snescpu.disasm import create_args


def test_create_args_default(rom):
    """Test create_args for DQ6 default values."""
    args, _ = create_args(rom, [])

    assert args["flags"] == 0
    assert args["first"] == 0xC00000
    assert args["last"] == -1
    assert not args["until_return"]


@pytest.mark.parametrize(
    "opcode,size",
    (
        (0x00, 3),
        (0x02, 1),
    ),
)
def test_specialized_state(fsm, opcode, size):
    """Test class `DisassembleStateDQ6`."""
    state = DisassembleStateDQ6(fsm)
    state.runtime_init()

    assert state.get_instruction(opcode).operand_size == size
