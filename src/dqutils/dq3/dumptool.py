#!/usr/bin/env python
"""dumptool.py: A dump tool for arrays of structured objects.

Usage:
dumptool.py ROM_ADDRESS SIZEOF_ARRAY SIZEOF_OBJECT [OPTIONS] <STDIN>

Example:
$ dumptool.py dqutils.dq3.dumptool 0xC8F323 0x36 10
#$0000\t#$00001F
#$0000\t#$0003E0
...
#$0035\t#$000001
[EOF]
"""
from __future__ import annotations

import sys
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from collections.abc import Sequence

from ..snescpu.dumptool import run

def main(args: Sequence[str]=sys.argv[1:]) -> int:
    return run('DRAGONQUEST3', args)

if __name__ == "__main__":
    sys.exit(main())
