# -*- coding: utf-8 -*-
"""Test suite for dqutils.

This test suite consists of a collection of test modules in the
dqutils.test package.  Each test module has a name starting with
'test' and contains a function test_suite().  The function is expected
to return an initialized unittest.TestSuite instance.

The modules are modeled after the ones of distutils.
"""

# The code below is taken from distutils.tests.__init__

import os
import sys
import unittest

HERE = os.path.dirname(__file__)

def test_suite():
    """Setup a test suite.
    """

    suite = unittest.TestSuite()
    for name in os.listdir(HERE):
        if name.startswith("test") and name.endswith(".py"):
            modname = "dqutils.test." + name[:-3]
            __import__(modname)
            module = sys.modules[modname]
            suite.addTest(module.test_suite())
    return suite

if __name__ == "__main__":
    unittest.main(defaultTest="test_suite")
