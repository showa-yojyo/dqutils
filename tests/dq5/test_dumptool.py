"""
Tests for dqutils.snescpu.dq5.dumptool
"""

from io import StringIO
from textwrap import dedent
from unittest import TestCase
from unittest.mock import patch
from dqutils.dq5.dumptool import main

class DumpToolTestCase(TestCase):

    def test_run(self):
        """A simple case"""

        input = StringIO(dedent(
            """\
            #$01:#$07
            #$02:#$07
            #$03:#$07
            #$04:#$07
            #$05:#$07
            #$06:#$07
            #$07:#$07
            #$08:#$07
            #$09:#$07
            #$0A:#$07
            #$0B:#$07
            """))
        with patch('sys.stdin', input), patch('sys.stdout', StringIO()) as output:
            main(['0x2396F3', '0x16', '10', '--delimiter', ':'])

        expected = dedent(
            """\
            0000:4:7:4:0:0:7:4:4:0:0:0
            0001:5:4:3:5:4:3:3:3:3:3:0
            0002:4:4:4:4:2:4:2:6:5:3:0
            0003:3:7:3:3:7:3:7:3:3:7:0
            0004:2:4:2:2:2:4:4:2:4:0:0
            0005:4:4:3:3:0:7:7:3:3:0:0
            0006:7:7:7:3:4:7:7:7:0:0:0
            0007:0:7:7:2:2:0:4:4:4:4:4
            0008:7:7:7:7:4:4:7:4:5:7:0
            0009:4:4:3:3:2:4:4:3:3:0:0
            """)
        self.assertMultiLineEqual(output.getvalue(), expected)
