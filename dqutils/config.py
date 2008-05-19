#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# $Id$

"""dqutils package config manager class
"""

import os.path
import ConfigParser


_MYCONFIG = None

def get_config():
    """TODO"""

    global _MYCONFIG
    if _MYCONFIG is None:
        _MYCONFIG = load_conf()
    return _MYCONFIG


# CONFIG ÇÉçÅ[Éh
def load_conf():
    """TODO"""

    confdir = confdir_home()
    if not os.path.isdir(confdir):
        raise IOError, 'no config ' + confdir

    conffile = os.path.join(confdir, 'config')
    if not os.path.exists(conffile):
        raise IOError, 'no config ' + conffile

    confparser = ConfigParser.ConfigParser()
    confparser.readfp(open(conffile))
    return confparser


def confdir_home():
    """TODO"""
    return os.path.expanduser('~/.dqutils')


if __name__ == "__main__":
    get_config()
    print 'dqutils config status: OK'
