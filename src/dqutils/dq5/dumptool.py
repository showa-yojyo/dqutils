#!/usr/bin/env python
"""dumptool.py: A dump tool for arrays of structured objects.

Usage:
dumptool.py ROM_ADDRESS SIZEOF_ARRAY SIZEOF_OBJECT [OPTIONS] <STDIN>

Example:
$ dumptool.py dqutils.dq5.dumptool 0x2396F3 0x16 0x55
#$00\t#$FF
#$01\t#$07
#$01\t#$38
#$01\t#$C0
...
#$15\t#$FF
[EOF]
"""

import sys

from dqutils.snescpu.dumptool import run


def main(args=sys.argv[1:]):
    run("DRAGONQUEST5", args)


if __name__ == "__main__":
    sys.exit(main())
