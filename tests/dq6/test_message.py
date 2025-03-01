"""Tests for dqutils.dq6.message"""

# ruff: noqa: RUF003
from array import array

import pytest

from dqutils.dq6.message import enum_battle, enum_scenario


def test_enum_battle():
    """Test function dqutils.dq6.enum_battle."""
    cpu_addr, code_seq = next(enum_battle(0x0140, 0x0141))

    # [BD]しかし なにも おこらなかった！[B1]
    however_nothing_happened = (
        b"\xbd\x1b\x15\x1b\x01\x24\x25\x32\x01\x14\x19\x36\x24\x15\x3e\x1f\x7a\xb1\xac"
    )

    assert cpu_addr == 0xF6F708
    assert however_nothing_happened == code_seq


@pytest.mark.parametrize(
    "first, last",
    [
        (0x0140, 0x0140),
        (0x00FF, 0x0020),
    ],
)
def test_enum_battle_invalid_range(first, last):
    with pytest.raises(StopIteration):
        next(enum_battle(first, last))


def test_enum_scenario():
    """Test function dqutils.dq6.enum_scenario."""
    # 0023:F7199F:08:にゃーん。
    # 0024:F719A4:40:にゃ～ん。
    # 0025:F719A9:10:にゃん にゃん にゃん！
    addrs = (0xF7199F, 0xF719A4, 0xF719A9)

    codes = (
        array("H", [0x0629, 0x0621, 0x0558, 0x04F7, 0x054C]),
        array("H", [0x0629, 0x0621, 0x0559, 0x04F7, 0x054C]),
        array(
            "H",
            [
                0x0629,
                0x0621,
                0x04F7,
                0x0200,
                0x0629,
                0x0621,
                0x04F7,
                0x0200,
                0x0629,
                0x0621,
                0x04F7,
                0x0551,
            ],
        ),
    )

    messages = zip(
        enum_scenario(0x0023, 0x0026),
        addrs,
        codes,
        strict=False,
    )
    for result, addr, code in messages:
        assert result[0] == addr
        # [-1] is one of the delimiter characters.
        assert result[-1][:-1] == code


@pytest.mark.parametrize(
    "first, last",
    [
        (0x0023, 0x0023),
        (0x00FF, 0x0020),
    ],
)
def test_enum_scenario_invalid_range(first, last):
    with pytest.raises(StopIteration):
        next(enum_scenario(first, last))
