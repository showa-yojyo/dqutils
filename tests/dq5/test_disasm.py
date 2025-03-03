"""Tests dqutils.snescpu.disasm for DQ5."""

from dqutils.snescpu.disasm import create_args

from .. import requires_config


@requires_config
def test_create_args_default(rom):
    args, _ = create_args(rom, [])

    assert args["flags"] == 0
    assert args["first"] == 0x008000
    assert args["last"] == -1
    assert not args["until_return"]
