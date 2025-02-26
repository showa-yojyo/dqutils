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


def test_bank(parser):
    """Test create_argparser for -b option."""

    args = parser.parse_args(["--bank", "C0"])
    assert args.bank == "C0"

    args = parser.parse_args(["-b", "C1"])
    assert args.bank == "C1"


def test_range(parser):
    """Test create_argparser for -r option."""

    args = parser.parse_args(["--range", "C2B09A:C2B0DD"])
    assert args.range == "C2B09A:C2B0DD"

    args = parser.parse_args(["-r", "C2B0DD"])
    assert args.range == "C2B0DD"


def test_until_return(parser):
    """Test create_argparser for -u option.

    Note that when -u and -r options are specified, the end
    of the range of offsets will be simply discarded.
    """

    args = parser.parse_args(["-u"])
    assert args.until_return
    assert args.until_return
