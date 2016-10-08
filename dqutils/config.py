#! /usr/bin/env python
"""This module provides functions that manage configuration data of
applications that use this package.
"""

import os.path
from configparser import ConfigParser

def get_config():
    """Return configuration data from :file:`config`.

    When the file :file:`config` is located under the path that
    :func:`confdir_home` returns, configuration data will be
    read from it and returned. Otherwise, an empty parser will be
    returned.

    Once configuration data is read and parsed, the data is cached
    internally and will be reused after the second invocation of
    :func:`get_config`.

    An example of the contents of :file:`config` is as follows::

      [ROM]
      DRAGONQUEST3 = /path/to/DRAGONQUEST3.smc
      DRAGONQUEST5 = /path/to/DRAGONQUEST5.smc
      DRAGONQUEST6 = /path/to/DRAGONQUEST6.smc

    Returns
    -------
    confparser : ConfigParser
        An object of the main configuration parser.
    """

    if not getattr(get_config, "MYCONFIG", None):
        get_config.MYCONFIG = _load_conf()

    return get_config.MYCONFIG

def _load_conf():
    """Read and parse configuration data from :file:`config`."""

    with open(os.path.join(confdir_home(), 'config')) as fin:
        confparser = ConfigParser()
        confparser.read_file(fin)

    return confparser

def confdir_home():
    """Return the path to dqutils configuration files.

    Default to :file:`~/.dqutils`.

    Returns
    -------
    path : str
        A string containing the path to the directory where
        configuration files of dqutils package locate in.
    """
    return os.path.expanduser('~/.dqutils')

if __name__ == "__main__":
    get_config()
    print('dqutils config status: OK')
