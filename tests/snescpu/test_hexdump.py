"""
Tests for dquils.snescpu.hexdump.
"""

import pytest

from dqutils.release import __version__ as dqutils_version
from dqutils.snescpu.hexdump import create_argparser


@pytest.fixture
def parser():
    return create_argparser()


def test_create_argparser(parser):
    """Test function `create_argparser`."""

    # invalid arguments
    invalid_arguments = (
        (),
        ("C0FF70"),
        ("C0FF70", "16"),
    )
    for args in invalid_arguments:
        with pytest.raises(SystemExit):
            parser.parse_args(args)

    # a normal case
    args = parser.parse_args(["C0FF70", "16", "4"])
    assert args.start == "C0FF70"
    assert args.byte_count == [16]
    assert args.record_count == 4


def test_version(parser, capture_stdout):
    """Test `--version`."""

    with pytest.raises(SystemExit) as ei:
        parser.parse_args(["--version"])
    assert ei.value.code == 0
    assert dqutils_version in capture_stdout.getvalue()


ADDRESS_PATTERN = r"^[0-9A-F]{2}/[0-9A-F]{4}:"
