"""
A simple hexdump.

Usage:
$ python -m dqutils.dq3.hexdump <address> <byte_count>... <record_count>
"""

from ..snescpu.hexdump import dump

if __name__ == "__main__":
    dump("DRAGONQUEST3")
