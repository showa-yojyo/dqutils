#! /usr/bin/env python
"""This module provides functions that manage configuration data of
applications that use this package.
"""

from collections.abc import Iterator
from configparser import ConfigParser
import os
from pathlib import Path

_CONFIG: ConfigParser | None = None

def get_config() -> ConfigParser:
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

    global _CONFIG
    if _CONFIG is None:
        _CONFIG = _load_conf()

    return _CONFIG

def _load_conf() -> ConfigParser:
    """Read and parse configuration data from :file:`config`."""

    with (confdir_home() / 'config').open() as fin:
        confparser = ConfigParser()
        confparser.read_file(fin)

    return confparser

def confdir_home() -> Path:
    """Return the directory path to dqutils configuration files.

    The directory location is determined in the following order:

    * On Linux,

      * ``$XDG_CONFIG_HOME/dqutils`` (if ``$XDG_CONFIG_HOME`` is defined)
      * Otherwise, ``$HOME/.config/dqutils``
    * On other platforms, * ``$HOME/.dqutils`` if ``$HOME`` is defined

    Returns
    -------
    path : str
        A string containing the path to the directory where configuration files
        of dqutils package locate in.
    """

    def gen_candidates() -> Iterator[Path]:
        if xdg_config_home := os.environ.get('XDG_CONFIG_HOME'):
            yield Path(xdg_config_home, "dqutils")
        home_dir = Path.home()
        yield home_dir / ".config" / "dqutils"
        yield home_dir / ".dqutils"

    for dir in gen_candidates():
        if dir.is_dir():
            return dir

    raise RuntimeError("Could not find configuration directory. See the README")

if __name__ == "__main__":
    get_config()
    print('dqutils config status: OK')
