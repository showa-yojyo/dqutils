# conftest.py

from io import StringIO

import pytest

from dqutils.snescpu.statemachine import StateMachine


@pytest.fixture()
def fsm_mock():
    return type("StateMachine", (object,), {})


@pytest.fixture
def fsm(state_classes, initial_state, rom):
    retval = StateMachine(state_classes, initial_state, rom)
    retval.destination = StringIO()
    yield retval
