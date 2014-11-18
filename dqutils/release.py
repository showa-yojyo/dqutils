# -*- coding: utf-8 -*-
"""dqutils.release - release information of dqutils.

This is modelled after (or a copy of) networkx.release.
"""
import os
import sys
import time
import datetime

# pylint: disable=import-error

_BASEDIR = os.path.abspath(os.path.split(__file__)[0])

_VERSION_TEMPLATE = '''\
# -*- coding: utf-8 -*-
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

def write_versionfile():
    """Create version.py in the package directory.

    This function is modelled after (or a copy of) the same name function
    defined in module networkx.release.

    Returns:
      (string): Version number.
    """

    version_file = os.path.join(_BASEDIR, 'version.py')
    if os.path.isfile(version_file):
        sys.path.insert(0, _BASEDIR)
        from version import version
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

def get_info(dynamic=True):
    """Get current information.

    This function is modelled after (or a copy of) the same name function
    defined in module networkx.release.

    Args:
      dynamic (bool): If dynamically get information.

    Returns:
      (tuple): Information for release, a tuple instance
        (date, date_info, version, version_info).
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
        version_info = (_NAME, _MAJOR, _MINOR, _MICRO)

    return date, date_info, version, version_info

# Version information
_NAME = 'dqutils'
_MAJOR = 1
_MINOR = 2
_MICRO = 0

# Declare current release as a development release.
_DEV = True
