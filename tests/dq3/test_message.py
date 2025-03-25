"""Tests for dqutils.dq3.message"""

# ruff: noqa: RUF003
from array import array

import pytest

from dqutils.dq3.message import enum_battle, enum_scenario

from .. import requires_config

pytestmark = requires_config


def test_enum_battle():
    """Test function dqutils.dq3.enum_battle."""
    cpuaddr, code_seq = next(enum_battle(0x0141, 0x0142))

    # [BD]しかし なにも おこらなかった！[B1]
    however_nothing_happened = b"\xbd\x17\x11\x17\x01\x20\x21\x2e\x01\x10\x15\x32\x20\x11\x3f\x1b\x7f\xb1\xac"

    assert cpuaddr == 0xFCBD36
    assert however_nothing_happened == code_seq


@pytest.mark.parametrize(
    ("msg_id", "addr", "expected"),
    zip(
        # 0160:FCD9D7:08:ぐがー ぐがー！
        # 0161:FCD9E0:80:ぐごー ぐごー！
        # 0162:FCD9E9:20:ぐがー ぐがー。
        range(0x0160, 0x0163),  # should call enum_scenario
        (0xFCD9D7, 0xFCD9E0, 0xFCD9E9),
        (
            array("H", [0x05DA, 0x053A, 0x0535, 0x0200, 0x05DA, 0x053A, 0x0535, 0x052E]),
            array("H", [0x05DA, 0x05DB, 0x0535, 0x0200, 0x05DA, 0x05DB, 0x0535, 0x052E]),
            array("H", [0x05DA, 0x053A, 0x0535, 0x0200, 0x05DA, 0x053A, 0x0535, 0x0529]),
        ),
        strict=False,
    ),
)
def test_enum_scenario(msg_id, addr, expected):
    """Test function dqutils.dq3.enum_scenario."""
    actual = next(iter(enum_scenario(msg_id, msg_id + 1)))

    assert actual[0] == addr
    # [-1] is one of the delimiter characters.
    assert actual[-1][:-1] == expected
