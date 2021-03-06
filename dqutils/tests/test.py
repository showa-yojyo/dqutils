#!/usr/bin/env python
"""Test runner for dqutils.

Implementation in this module is taken from networkx.tests.test
module.
"""
import sys
from os import (getcwd, path)

def run(verbosity=1, doctest=False):
    """Run dqutils tests.

    Parameters
    ----------
    verbosity : int, optional, default: 1
        Level of detail in test reports. Higher numbers provide
        more detail.

    doctest : bool, optional, default: False
        True to run doctests in code modules.

    Returns
    -------
    status : bool
        True on success, false on failure.
    """

    try:
        import nose
    except ImportError:
        raise ImportError("The nose package is needed.")

    print("Running dqutils tests:", file=sys.stderr)
    install_dir = path.join(path.dirname(__file__), path.pardir)

    # Stop if running from source directory.
    if getcwd() == path.abspath(path.join(install_dir, path.pardir)):
        raise RuntimeError(
            "Can't run tests from source directory.\n"
            "Run 'nosetests' from the command line.")

    argv = [' ',
            '--verbosity={:d}'.format(verbosity),
            '--where', install_dir,
            '-exe']
    if doctest:
        argv.extend(['--with-doctest', '--doctest-extension=txt'])

    return nose.run(argv=argv)

if __name__ == "__main__":
    run()
