"""Tests for dqutils.dq3.string"""

import pytest

from dqutils.dq3.string import CONTEXT, enum_string
from dqutils.string import get_text

from .. import requires_config

pytestmark = requires_config


def test_get_text():
    """Test function dqutils.dq3.get_text."""
    text = get_text(
        b"\x26\x24\x12\x24\xdc\x0e\xac",
        CONTEXT["charmap"],
        CONTEXT["delimiters"],
    )
    assert "ひのきのぼう" in text


@pytest.mark.parametrize(
    ("str_id", "expected"),
    zip(
        range(0x100, 0x110),  # should use enum_string
        (
            "FED659:せいすい",
            "FED65E:キメラのつばさ",
            "FED666:せかいじゅのは",
            "FED66E:しのオルゴール",
            "FED676:あいのおもいで",
            "FED67E:まんげつそう",
            "FED685:みずでっぽう",
            "FED68C:ふなのりのほね",
            "FED694:やまびこのふえ",
            "FED69C:ようせいのふえ",
            "FED6A4:ぎんのたてごと",
            "FED6AC:ひかりのたま",
            "FED6B3:どくがのこな",
            "FED6BA:まだらくもいと",
            "FED6C2:たいようのいし",
            "FED6CA:にじのしずく",
        ),
        strict=False,
    ),
)
def test_enum_string(str_id, expected):
    """Test function dqutils.dq3.enum_string."""
    actual = next(iter(enum_string(str_id, str_id + 1)))

    expected_address, expected_readable = expected.split(":")
    assert actual[0] == int(expected_address, 16)
    assert expected_readable in get_text(
        actual[1],
        CONTEXT["charmap"],
        CONTEXT["delimiters"],
    )
