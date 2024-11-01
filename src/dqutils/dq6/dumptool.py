#!/usr/bin/env python
"""dumptool.py: A dump tool for arrays of structured objects.

Usage:
dumptool.py ROM_ADDRESS SIZEOF_ARRAY SIZEOF_OBJECT [OPTIONS] <STDIN>

Example:
$ dumptool.py dqutils.dq6.dumptool 0xC8C65D 0x19 0x019A
#$00\t#$0001
#$00\t#$00FE
...
#$15\t#$FFFF
#$17\t#$FFFF
[EOF]
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Sequence

from ..snescpu.dumptool import run


def main(args: Sequence[str] = sys.argv[1:]) -> int:
    return run("DRAGONQUEST6", args)


if __name__ == "__main__":
    sys.exit(main())
