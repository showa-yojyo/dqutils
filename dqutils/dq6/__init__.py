# -*- coding: utf-8 -*-
#
# $Id$
"""dqutils package - dq6
"""

def open_rom(mode = 'rb'):
    from dqutils.config import get_config
    confparser = get_config()
    rompath = confparser.get('ROM', 'DRAGONQUEST6')

    import os.path
    if not os.path.exists(rompath):
        raise IOError, 'Not found ROM ' + rompath

    return open(rompath, mode)
