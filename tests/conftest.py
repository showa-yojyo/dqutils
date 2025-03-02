# conftest.py

import sys
from io import StringIO

import pytest

from dqutils.snescpu.statemachine import StateMachine


@pytest.fixture
def capture_stdout(monkeypatch):
    out = StringIO()

    def write_wrapper(s):
        out.write(s)
        return out

    monkeypatch.setattr(sys.stdout, "write", write_wrapper)
    return out


@pytest.fixture
def capture_stderr(monkeypatch):
    out = StringIO()

    def write_wrapper(s):
        out.write(s)
        return out

    monkeypatch.setattr(sys.stderr, "write", write_wrapper)
    return out


@pytest.fixture()
def fsm_mock():
    return type("StateMachine", (object,), {})


@pytest.fixture
def fsm(state_classes, initial_state, rom):
    retval = StateMachine(state_classes, initial_state, rom)
    retval.destination = StringIO()
    yield retval
