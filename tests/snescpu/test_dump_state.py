"""
Tests for dqutils.snescpu.states.DumpState
"""

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


def test_runtime_init(fsm_mock):
    """
    Test behavior of `DumpState.runtime_init`.
    """

    state = DumpState(fsm_mock)
    state.runtime_init(byte_count=[20], record_count=47894)
    assert state.byte_count == [20]
    assert state.record_count == 47894

    state.runtime_init()
    assert state.byte_count == ()
    assert state.record_count == 0
