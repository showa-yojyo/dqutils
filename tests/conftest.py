# conftest.py

import sys
from io import StringIO

import pytest

from dqutils.snescpu.statemachine import StateMachine


# Use for dq{3,5,6}/test_hexdump.py
@pytest.fixture
def capture_stdout(monkeypatch):
    out = StringIO()

    def write_wrapper(s):
        out.write(s)
        return out

    monkeypatch.setattr(sys.stdout, "write", write_wrapper)
    return out


@pytest.fixture()
def fsm_mock():
    return type("StateMachine", (object,), {})


@pytest.fixture
def fsm(state_classes, initial_state, rom):
    retval = StateMachine(state_classes, initial_state, rom)
    retval.destination = StringIO()
    yield retval
