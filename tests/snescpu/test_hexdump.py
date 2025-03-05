"""
Tests for dquils.snescpu.hexdump.
"""

import pytest

from dqutils.release import __version__ as dqutils_version
from dqutils.snescpu.hexdump import create_argparser

ADDRESS_PATTERN = r"^[0-9A-F]{2}/[0-9A-F]{4}:"


@pytest.fixture
def parser():
    return create_argparser()


@pytest.mark.parametrize(
    "invalid_args",
    (
        (),
        ("C0FF70"),
        ("C0FF70", "16"),
    ),
)
def test_invalid_args(parser, invalid_args):
    with pytest.raises(SystemExit) as ei:
        parser.parse_args(invalid_args)
    assert ei.value.code == 2


@pytest.mark.parametrize(
    "valid_args",
    (("C0FF70", "16", "4"),),
)
def test_valid_args(parser, valid_args):
    args = parser.parse_args(valid_args)
    assert args.start == valid_args[0]
    assert args.byte_count == [int(valid_args[1])]
    assert args.record_count == int(valid_args[2])


def test_version(parser, capsys):
    """Test `--version`."""

    with pytest.raises(SystemExit) as ei:
        parser.parse_args(["--version"])
    assert ei.value.code == 0
    assert dqutils_version in capsys.readouterr().out
