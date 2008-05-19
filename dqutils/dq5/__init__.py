# -*- coding: utf-8 -*-
#
# $Id$
"""dqutils package - dq5
"""

def open_rom(mode = 'rb'):
    """Help me"""
    from dqutils.config import get_config
    confparser = get_config()
    rompath = confparser.get('ROM', 'DRAGONQUEST5')

    import os.path
    if not os.path.exists(rompath):
        raise IOError, 'Not found ROM ' + rompath

    return open(rompath, mode)
