"""
Tests for dqutils.snescpu.states.DumpState
"""

import pytest

from dqutils.snescpu.states import DumpState


def test_initial_properties(fsm_mock):
    """
    Test the initial condition of an object of class
    `DumpState`.
    """

    state = DumpState(fsm_mock)
    assert state.state_machine == fsm_mock
    assert state.byte_count == ()
    assert state.record_count == 0


@pytest.mark.parametrize(
    "init_kwargs,byte_count,record_count",
    (
        [{}, (), 0],
        [{"byte_count": 20, "record_count": 47894}, (20), 47894],
    ),
)
def test_runtime_init(fsm_mock, init_kwargs, byte_count, record_count):
    """
    Test behavior of `DumpState.runtime_init`.
    """

    state = DumpState(fsm_mock)
    state.runtime_init(**init_kwargs)
    assert state.byte_count == byte_count
    assert state.record_count == record_count
