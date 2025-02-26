# conftest.py

import sys
from io import StringIO

import pytest


# Use for dq{3,5,6}/test_hexdump.py
@pytest.fixture(scope="function")
def capture_stdout(monkeypatch):
    out = StringIO()

    def write_wrapper(s):
        out.write(s)
        return out

    monkeypatch.setattr(sys.stdout, "write", write_wrapper)
    return out
