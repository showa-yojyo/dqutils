"""
A simple hexdump.

Usage:
$ python -m dqutils.dq5.hexdump <address> <byte_count>... <record_count>
"""

from dqutils.snescpu.hexdump import dump

if __name__ == "__main__":
    dump("DRAGONQUEST5")
