"""dqutils.release - release information of dqutils.

This is modelled after (or a copy of) networkx.release.
"""
from __future__ import annotations

import datetime
import os
import sys
import time
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import Final, TypeAlias

# pylint: disable=import-error

_BASEDIR = os.path.abspath(os.path.split(__file__)[0])

_VERSION_TEMPLATE: Final[str] = '''\
"""dqutils.version - version information of dqutils."""

import datetime

# pylint: disable=invalid-name

version = "{version}"
date = "{date}"

# True if this is development version.
dev = {dev}

# Format: (name, major, minor, micro)
version_info = {version_info!r}

# Format: a 'datetime.datetime' instance
date_info = {date_info!r}
'''

def write_versionfile() -> str:
    """Create version.py in the package directory.

    This function is modelled after (or a copy of) the same name function
    defined in module networkx.release.

    Returns
    -------
    version : string
        The version number.
    """

    version_file = os.path.join(_BASEDIR, 'version.py')
    if os.path.isfile(version_file):
        sys.path.insert(0, _BASEDIR)
        from dqutils.version import version
        del sys.path[0]
        return version

    # Try to update all information
    date, date_info, version, version_info = get_info()

    with open(version_file, mode='w', newline='') as fout:
        fout.write(_VERSION_TEMPLATE.format(
            dev=_DEV,
            version=version,
            version_info=version_info,
            date=date,
            date_info=date_info,))

    return version

if TYPE_CHECKING:
    VersionInfo: TypeAlias = tuple[str, int, int, int]

def get_info(dynamic=True) -> tuple[str, datetime.datetime, str, VersionInfo]:
    """Get current information.

    This function is modelled after (or a copy of) the same name function
    defined in module networkx.release.

    Parameters
    ----------
    dynamic : bool, optional, default:True
        True if dynamically get information.

    Returns
    -------
    date : str
    date_info : datetime.datetime
    version : str
    version_info : tuple of str
    """

    import_failed = False
    if not dynamic:
        sys.path.insert(0, _BASEDIR)
        try:
            from version import date, date_info, version, version_info
        except ImportError:
            import_failed = True
        del sys.path[0]

    if import_failed or dynamic:
        date_info = datetime.datetime.now()
        date = time.asctime(date_info.timetuple())
        version = '.'.join([str(i) for i in (_MAJOR, _MINOR, _MICRO)])
        if _DEV:
            version += 'dev'
        version_info = (NAME, _MAJOR, _MINOR, _MICRO)

    return date, date_info, version, version_info

# Version information
NAME: Final[str] = 'dqutils'
_MAJOR: Final[int] = 1
_MINOR: Final[int] = 1
_MICRO: Final[int] = 2

# Declare current release as a development release.
_DEV: Final[bool] = True

# Constants mainly for setup.py.

DESCRIPTION: Final[str] = 'dqutils (Dragon Quest Utilities)'
#LONG_DESCRIPTION

LICENSE: Final[str] = 'MIT'

# Author details.
AUTHOR: Final[str] = 'プレハブ小屋'
AUTHOR_EMAIL: Final[str] = 'yojyo@hotmail.com'

#MAINTAINER
#MAINTAINER_EMAIL

# The project's main homepage.
URL: Final[str] = 'https://github.com/showa-yojyo/dqutils'
DOWNLOAD_URL: Final[str] = 'https://github.com/showa-yojyo/dqutils'

PLATFORMS: Final[tuple[str, ...]] = (
    'Linux',
    'Mac OSX',
    'Windows',
    'Unix',)

# What does your project relate to?
KEYWORDS: Final[tuple[str, ...]] = ('DRAGON QUEST SNES',)

# See https://pypi.python.org/pypi?%3Aaction=list_classifiers
CLASSIFIERS: Final[tuple[str, ...]] = (
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 3 - Alpha',

    # Indicate who your project is intended for.
    'Intended Audience :: Other Audience',
    'Topic :: Utilities',

    # Pick your license as you wish (should match "license" above)
    'License :: OSI Approved :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 3.12',)

DATE, DATE_INFO, VERSION, VERSION_INFO = get_info()
