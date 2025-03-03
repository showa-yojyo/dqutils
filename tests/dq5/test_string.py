"""Tests for dqutils.dq5.string"""

import pytest

from dqutils.dq5.charsmall import process_dakuten
from dqutils.dq5.string import CONTEXT_GROUP, enum_string
from dqutils.string import get_text

from .. import requires_config

pytestmark = requires_config

HINOKINOBOU = b"\x2a\x28\x16\x28\x84\x2d\x12"


def test_enum_string():
    """Test function dqutils.dq5.enum_string."""
    context = CONTEXT_GROUP[5]

    addr, code_seq = next(iter(enum_string(context, 0, 1)))
    assert addr == 0x23CE0E
    assert code_seq == HINOKINOBOU


@pytest.mark.parametrize("ctx", CONTEXT_GROUP)
def test_enum_string_0_0(ctx):
    """Test enum_string(?, 0, 0)"""
    if ctx["string_id_last"] == 0:
        assert ctx["string_id_first"] == 0
        with pytest.raises(StopIteration):
            next(enum_string(ctx))


def test_make_text():
    """Test function dqutils.dq5.charmapsmall.process_dakuten."""
    context = CONTEXT_GROUP[5]
    charmap = context["charmap"]

    text = process_dakuten(get_text(HINOKINOBOU, charmap, None))
    assert text == "ひのきのぼう"
