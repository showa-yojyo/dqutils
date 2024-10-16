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

import sys
from ..snescpu.dumptool import run

def main(args=sys.argv[1:]):
    run('DRAGONQUEST3', args)

if __name__ == "__main__":
    sys.exit(main())
