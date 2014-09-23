# -*- coding: utf-8 -*-
#
"""dqutils package - dqutils.dq5 __init__ module
"""

from dqutils.config import get_config

def open_rom():
    """Open the DRAGONQUEST5 ROM image by using the setting file."""

    rompath = get_config().get('ROM', 'DRAGONQUEST5')
    return open(rompath, mode='rb')
