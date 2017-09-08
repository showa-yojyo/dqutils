"""
Tests for dqutils.snescpu.dq6.dumptool
"""

from io import StringIO
from textwrap import dedent
from unittest import TestCase
from unittest.mock import patch
from ..dumptool import main

class DumpToolTestCase(TestCase):

    def test_run(self):
        """A simple case"""

        input = StringIO(dedent(
            """\
            #$00:#$0001
            #$00:#$00FE
            #$01:#$0001
            #$01:#$00FE
            #$02:#$0001
            #$02:#$00FE
            """))
        with patch('sys.stdin', input), patch('sys.stdout', StringIO()) as output:
            main(['0xC8C65D', '0x19', '10', '--delimiter', ':'])

        print(output.getvalue())

        expected = dedent(
            """\
            0000:0:00:0:00:0:00
            0001:1:01:0:01:0:0E
            0002:1:01:0:01:0:0E
            0003:1:01:0:01:0:0E
            0004:1:02:0:02:0:0F
            0005:1:02:0:02:0:0F
            0006:1:02:0:02:0:0F
            0007:1:03:0:03:0:10
            0008:1:03:0:03:0:10
            0009:1:03:0:03:0:10
            """)
        self.assertMultiLineEqual(output.getvalue(), expected)
