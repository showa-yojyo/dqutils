"""
Tests for dqutils.snescpu.states.DumpState
"""

from unittest.mock import Mock

import pytest

from dqutils.snescpu.states import DumpState


@pytest.fixture
def fsm():
    return Mock(program_counter="dummy")


def test_initial_properties(fsm):
    """
    Test the initial condition of an object of class
    `DumpState`.
    """

    fsm = Mock(program_counter="dummy")
    state = DumpState(fsm)
    assert state.state_machine == fsm
    assert state.byte_count == ()
    assert state.record_count == 0


def test_runtime_init(fsm):
    """
    Test behavior of `DumpState.runtime_init`.
    """

    fsm = Mock(program_counter="dummy")
    state = DumpState(fsm)
    state.runtime_init(byte_count=[20], record_count=47894)
    assert state.byte_count == [20]
    assert state.record_count == 47894

    state.runtime_init()
    assert state.byte_count == ()
    assert state.record_count == 0
