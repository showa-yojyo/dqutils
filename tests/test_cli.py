"""
Tests for dqutils.dq3.main
"""

import sys
from io import StringIO
from unittest import TestCase
from unittest.mock import patch

_ARG0 = sys.argv[0]


class AbstractRunTestCase(TestCase):
    """Test functions for dqutils.dq{3,5,6}.main"""

    def _test_main_helper(self, main, *args):
        with (
            patch("sys.stdout", StringIO()) as output,
            self.assertRaises(SystemExit) as cm,
            patch("sys.argv", [_ARG0, *args]),
        ):
            main()
            self.assertEqual(cm.exception.code, 0)
            self.assertIn("usage", output.getvalue())
