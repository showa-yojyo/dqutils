"""
A simple hexdump.

Usage:
$ python -m dqutils.dq6.hexdump <address> <byte_count> <record_count>
"""

from dqutils.snescpu.hexdump import main

if __name__ == '__main__':
    main('DRAGONQUEST6')
