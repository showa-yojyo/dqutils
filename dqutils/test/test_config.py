#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for dqutils.config
"""

import os
import unittest

import dqutils.config

class ConfigTestCase(unittest.TestCase):

    def test_config(self):
        """TODO
        """
        self.assertEqual(1, 1)

    def test_get_config(self):
        """TODO
        """
        
        self.assertEqual(2, 2)

    def test_set_config(self):
        """TODO
        """
        
        self.assertEqual(4, 4)

def test_suite():
    return unittest.makeSuite(ConfigTestCase)

if __name__ == "__main__":
    unittest.main(defaultTest="test_suite")

