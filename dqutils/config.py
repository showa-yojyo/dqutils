#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""dqutils package config manager class
"""

import os.path
import configparser

def get_config():
    """Return the configuration object."""

    if not getattr(get_config, "MYCONFIG", None):
        get_config.MYCONFIG = load_conf()

    return get_config.MYCONFIG

def load_conf():
    """Read user's setting file."""

    confdir = confdir_home()
    conffile = os.path.join(confdir, 'config')
    confparser = configparser.ConfigParser()
    with open(conffile) as fin:
        confparser.read_file(fin)
    return confparser

def confdir_home():
    """Return the directory that contain the configuration files."""
    return os.path.expanduser('~/.dqutils')

if __name__ == "__main__":
    get_config()
    print('dqutils config status: OK')
