#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for dqutils.config
"""

import unittest
#import dqutils.config

# pylint: disable=too-many-public-methods
class ConfigTestCase(unittest.TestCase):
    """Test functions defined in dqutils.config."""
    pass

def test_suite():
    """Setup a test suite."""
    return unittest.makeSuite(ConfigTestCase)

if __name__ == "__main__":
    unittest.main(defaultTest="test_suite")
