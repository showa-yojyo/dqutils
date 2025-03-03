"""Tests for dqutils.snescpu.disasm for DQ3."""

import pytest

from dqutils.dq3.disasm import DisassembleStateDQ3
from dqutils.snescpu.disasm import create_args


def test_create_args_default(rom):
    """Test create_args for DQ3 default values."""
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
    """Test class `DisassembleStateDQ3`."""
    state = DisassembleStateDQ3(fsm)
    state.runtime_init()

    assert state.get_instruction(opcode).operand_size == size
