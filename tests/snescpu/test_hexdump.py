"""
Tests for dquils.snescpu.hexdump.
"""

from io import StringIO
from os import devnull
from unittest import TestCase
from unittest.mock import patch

from dqutils.release import __version__ as dqutils_version
from dqutils.snescpu.hexdump import create_argparser


class HexDumpTestCase(TestCase):
    """Tests for dquils.snescpu.hexdump."""

    def setUp(self):
        self.parser = create_argparser()

    def tearDown(self):
        del self.parser
        self.parser = None

    def test_create_argparser(self):
        """Test function `create_argparser`."""

        parser = self.parser

        # invalid arguments
        with open(devnull, "w") as fout, patch("sys.stderr", fout):
            self.assertRaises(SystemExit, parser.parse_args)
            self.assertRaises(SystemExit, parser.parse_args, ["C0FF70"])
            self.assertRaises(SystemExit, parser.parse_args, ["C0FF70", "16"])

        # a normal case
        args = parser.parse_args(["C0FF70", "16", "4"])
        self.assertEqual(args.start, "C0FF70")
        self.assertEqual(args.byte_count, [16])
        self.assertEqual(args.record_count, 4)

    def test_version(self):
        """Test `--version`."""

        parser = self.parser
        with (
            patch("sys.stdout", StringIO()) as output,
            self.assertRaises(SystemExit) as cm,
        ):
            parser.parse_args(["--version"])
        self.assertEqual(cm.exception.code, 0)
        self.assertIn(dqutils_version, output.getvalue())


ADDRESS_PATTERN = r"^[0-9A-F]{2}/[0-9A-F]{4}:"


class AbstractHexDumpTestCase(TestCase):
    """The base class of HexDumpTestCase subclasses."""

    game_title = None

    def __init__(self, method_name="runTest"):
        super().__init__(methodName=method_name)
        self.patcher = None
        self.out = None

    def setUp(self):
        self.patcher = patch("sys.stdout", new_callable=StringIO)
        self.out = self.patcher.start()

    def tearDown(self):
        self.patcher.stop()
        self.patcher = None
