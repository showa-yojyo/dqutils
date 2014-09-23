# -*- coding: utf-8 -*-

"""dqutils package - dqutils.dq3 __init__ module
"""

from dqutils.config import get_config

def open_rom():
    """Open the DRAGONQUEST3 ROM image by using the setting file."""

    rompath = get_config().get('ROM', 'DRAGONQUEST3')
    return open(rompath, mode='rb')
