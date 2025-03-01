"""
Tests for dqutils.snescpu.disasm.
"""

import pytest

from dqutils.snescpu.disasm import create_argparser


@pytest.fixture
def parser():
    return create_argparser()


def test_default_settings(parser):
    """Test create_argparser for no argument."""
    args = parser.parse_args([])

    assert not args.accumulator_8bit
    assert not args.index_8bit
    assert not args.bank
    assert not args.range
    assert not args.until_return


def test_accum_flag(parser):
    """Test create_argparser for -a options."""

    args = parser.parse_args(["-a"])
    assert args.accumulator_8bit
    assert not args.index_8bit


def test_index_flag(parser):
    """Test create_argparser for -x options."""

    args = parser.parse_args(["-x"])
    assert not args.accumulator_8bit
    assert args.index_8bit


@pytest.mark.parametrize(
    "args,expected",
    (
        (("--bank", "C0"), "C0"),
        (("-b", "C1"), "C1"),
    ),
)
def test_bank(parser, args, expected):
    """Test create_argparser for -b, --bank option."""

    assert parser.parse_args(args).bank == expected


@pytest.mark.parametrize(
    "args,expected",
    (
        (["--range", "C2B09A:C2B0DD"], "C2B09A:C2B0DD"),
        (["-r", "C2B0DD"], "C2B0DD"),
    ),
)
def test_range(parser, args, expected):
    """Test create_argparser for -r, --range option."""

    assert parser.parse_args(args).range == expected


def test_until_return(parser):
    """Test create_argparser for -u option.

    Note that when -u and -r options are specified, the end of the range of offsets will
    be simply discarded.
    """

    args = parser.parse_args(["-u"])
    assert args.until_return
