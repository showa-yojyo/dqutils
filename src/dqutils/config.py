#! /usr/bin/env python
"""This module provides functions that manage configuration data of
applications that use this package.
"""

from __future__ import annotations

import os
import sys
from configparser import ConfigParser
from pathlib import Path
from typing import TYPE_CHECKING, Self

if TYPE_CHECKING:
    from collections.abc import Iterator


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

    return _CONFIG


def _load_conf() -> ConfigParser:
    """Read and parse configuration data from :file:`config`."""

    with (confdir_home() / "config").open() as fin:
        confparser = ConfigParser()
        confparser.read_file(fin)

    return confparser


class ConfigNotFoundError(Exception):
    def __init__(self: Self) -> None:
        super().__init__("Could not find configuration directory.")


def confdir_home() -> Path:
    """Return the directory path to dqutils configuration files.

    The directory location is determined in the following order:

    * On Linux,

      * ``$XDG_CONFIG_HOME/dqutils`` (if ``$XDG_CONFIG_HOME`` is defined)
      * Otherwise, ``$HOME/.config/dqutils``
    * On other platforms, ``$HOME/.dqutils`` if ``$HOME`` is defined

    Returns
    -------
    path : str
        A string containing the path to the directory where configuration files
        of dqutils package locate in.
    """

    def gen_candidates() -> Iterator[Path]:
        if xdg_config_home := os.environ.get("XDG_CONFIG_HOME"):
            yield Path(xdg_config_home, "dqutils")
        home_dir = Path.home()
        yield home_dir / ".config" / "dqutils"
        yield home_dir / ".dqutils"

    for d in gen_candidates():
        if d.is_dir():
            return d

    raise ConfigNotFoundError


_CONFIG: ConfigParser | None
try:
    _CONFIG = _load_conf()
except ConfigNotFoundError:
    _CONFIG = None


if __name__ == "__main__":
    sys.exit(1 if get_config() else 0)
