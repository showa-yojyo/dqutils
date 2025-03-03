"""
Tests for dqutils.snescpu.states.DisassembleState.
"""

import pytest

from dqutils.snescpu.instructions import DEFAULT_INSTRUCTIONS
from dqutils.snescpu.states import DisassembleState


def test_initial_properties(fsm_mock):
    """
    Test the initial condition of an object of class `DisassembleState`.
    """

    state = DisassembleState(fsm_mock)
    assert state.state_machine == fsm_mock
    assert state.current_opcode is None
    assert state.current_operand is None
    assert state.current_operand_size == 0
    assert state.flags == 0
    assert not state.until_return
    assert tuple(state.instructions) == tuple(DEFAULT_INSTRUCTIONS)


def test_runtime_init(fsm_mock):
    """
    Test behaviors of `DisassembleState.runtime_init`.
    """

    state = DisassembleState(fsm_mock)

    # The default behavior.
    state.runtime_init()
    assert state.current_opcode is None
    assert state.current_operand is None
    assert state.current_operand_size == 0
    assert state.flags == 0
    assert not state.until_return

    # Specify some keyword arguments.
    state.runtime_init(flags=0x30, until_return=True)
    assert state.flags == 0x30
    assert state.until_return


@pytest.mark.parametrize("opcode,index", ([0x00, 0], [b"\x03", 3]))
def test_get_instruction(fsm_mock, opcode, index):
    """
    Test behaviors of `DisassembleState.get_instruction`.
    """

    state = DisassembleState(fsm_mock)
    state.runtime_init()

    assert state.get_instruction(opcode) == DEFAULT_INSTRUCTIONS[index]
