"""Tests for dqutils.dq6.string"""

import pytest

from dqutils.dq6.string import CONTEXT, enum_string
from dqutils.string import get_text

from .. import requires_config

pytestmark = requires_config


def test_get_text():
    """Test function dqutils.dq6.get_text."""
    text = get_text(
        b"\x2a\x28\x16\x28\xdc\x12\xac",
        CONTEXT["charmap"],
        CONTEXT["delimiters"],
    )
    assert "ひのきのぼう" in text


@pytest.mark.parametrize(
    "id,expected",
    zip(
        range(0x300, 0x310),  # should be use enum_string
        (
            "FB97DB:ムドー",
            "FB97DF:しれんその１",
            "FB97E6:モンストラー",
            "FB97ED:スコット",
            "FB97F2:ホリディ",
            "FB97F7:ガルシア",
            "FB97FC:ブラスト",
            "FB9801:じごくのもんばん",
            "FB980A:ジャミラス",
            "FB9810:ヘルクラウド",
            "FB9817:ミラルゴ",
            "FB981C:グラコス",
            "FB9821:まおうのつかい",
            "FB9829:テリー",
            "FB982D:まおうのつかい",
            "FB9835:デュラン",
        ),
    ),
)
def test_enum_string(id, expected):
    """Test function dqutils.dq6.enum_string."""
    actual = next(iter(enum_string(id, id + 1)))

    expected_address, expected_readable = expected.split(":")
    assert actual[0] == int(expected_address, 16)
    assert expected_readable in get_text(
        actual[1],
        CONTEXT["charmap"],
        CONTEXT["delimiters"],
    )
