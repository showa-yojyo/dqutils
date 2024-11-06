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

    def test_shop_data(self):
        data = StringIO(
            "#$00:#$007F\n"
            "#$00:#$0080\n"
            "#$01:#$00FF\n"
            "#$02:#$00FF\n"
            "#$03:#$00FF\n"
            "#$04:#$00FF\n"
            "#$05:#$00FF\n"
            "#$06:#$00FF\n"
            "#$07:#$00FF\n"
        )
        expected = (
            "0000:06:1:08:1A:19:10:18:21:03\n"
            "0001:02:1:77:B8:B9:BA:BB:00:00\n"
            "0002:00:0:36:03:0D:3E:3F:55:79\n"
            "0003:02:1:B8:B9:BA:BB:BF:00:00\n"
            "0004:00:0:07:06:22:41:66:5C:00\n"
        )
        with patch("sys.stdin", data), patch("sys.stdout", StringIO()) as output:
            main(["0xC30900", "8", "5", "--delimiter", ":"])
        # self.maxDiff = None
        self.assertMultiLineEqual(output.getvalue(), expected)
