"""
Tests for dqutils.snescpu.dq3.dumptool
"""

from io import StringIO
from textwrap import dedent
from unittest import TestCase
from unittest.mock import patch

from dqutils.dq3.dumptool import main


class DumpToolTestCase(TestCase):
    def test_run(self):
        """A simple case"""

        data = StringIO(
            dedent(
                """\
            #$0000:#$00001F
            #$0000:#$0003E0
            #$0001:#$00007C
            #$0001:#$000F80
            #$0002:#$0001F0
            #$0003:#$000FC0
            """
            )
        )
        with patch("sys.stdin", data), patch("sys.stdout", StringIO()) as output:
            main(["0xC8F323", "0x36", "10", "--delimiter", ":"])

        expected = dedent(
            """\
            0000:01:02:01:06:04:10
            0001:01:01:01:06:05:10
            0002:01:02:01:04:05:10
            0003:01:02:01:04:05:10
            0004:01:08:02:08:0C:20
            0005:01:08:02:08:0C:20
            0006:02:03:01:02:07:10
            0007:02:03:01:02:07:10
            0008:02:03:01:02:07:10
            0009:02:03:01:02:07:10
            """
        )
        self.assertMultiLineEqual(output.getvalue(), expected)
