# -*- coding: utf-8 -*-

"""dqutils package - dqutils.dq6 __init__ module
"""

from dqutils.config import get_config

def open_rom():
    """Open the DRAGONQUEST6 ROM image by using the setting file."""

    rompath = get_config().get('ROM', 'DRAGONQUEST6')
    return open(rompath, mode='rb')
