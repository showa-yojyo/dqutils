"""Tests for dqutils.dq5.message"""

# ruff: noqa: RUF003
from array import array

import pytest

from dqutils.dq5.message import enum_battle, enum_scenario

from .. import requires_config

pytestmark = requires_config


def test_enum_battle():
    """Test function dqutils.dq5.enum_battle."""
    cpu_addr, _, code_seq = next(iter(enum_battle(0x007B, 0x007C)))

    # しかし なにも おこらなかった！[FE]
    however_nothing_happened = array(
        "H",
        (
            0x1B,
            0x15,
            0x1B,
            0x01,
            0x24,
            0x25,
            0x32,
            0x01,
            0x14,
            0x19,
            0x36,
            0x24,
            0x15,
            0x3E,
            0x1F,
            0x7A,
            0xFE,
        ),
    )

    assert cpu_addr == 0x078647
    assert however_nothing_happened == code_seq


@pytest.mark.parametrize(
    "first, last",
    [
        (0x007C, 0x007C),
        (0x00FF, 0x0020),
    ],
)
def test_enum_battle_invalid_range(first, last):
    with pytest.raises(StopIteration):
        next(enum_battle(first, last))


def test_enum_scenario():
    """Test function dqutils.dq5.enum_scenario."""
    cpu_addr, _, code_seq = next(iter(enum_scenario(0x0B95, 0x0B96)))

    # 0B95:0BCCD8:02:わーい わーい！
    wai = array(
        "H", (0x031B, 0x0360, 0x0398, 0x0000, 0x031B, 0x0360, 0x0398, 0x035A, 0x1001)
    )

    assert cpu_addr == 0x0BCCD8
    assert wai == code_seq


@pytest.mark.parametrize(
    "first, last",
    [
        (0x0B95, 0x0B95),
        (0x00FF, 0x0020),
    ],
)
def test_enum_scenario_invalid_range(first, last):
    with pytest.raises(StopIteration):
        next(enum_scenario(first, last))
