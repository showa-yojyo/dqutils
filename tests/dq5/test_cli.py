"""
Tests for dqutils.dq5.main
"""

from test_cli import AbstractRunTestCase

from dqutils.dq5 import main


class RunTestCase(AbstractRunTestCase):
    """Test functions for dqutils.dq5.main"""

    def test_main_no_args(self):
        self._test_main_helper(main)

    def test_main_help(self):
        self._test_main_helper(main, "--help")
