# conftest.py

from io import StringIO

import pytest

from dqutils.snescpu.statemachine import StateMachine


@pytest.fixture
def fsm_mock():
    """Return a mock object of :class:`StateMachine`."""
    return type("StateMachine", (object,), {})


@pytest.fixture
def fsm(state_classes, initial_state, rom):
    """Return an object of :class:`StateMachine`.

    Parameters
    ----------
    :param state_classes: A list of :class:`State` subclasses.
    :param initial_state: The class's name of the initial state.
    :param rom: A ROM image object.
    """
    retval = StateMachine(state_classes, initial_state, rom)
    retval.destination = StringIO()
    return retval
