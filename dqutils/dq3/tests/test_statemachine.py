"""
Tests for dqutils.snescpu.statemachine.
"""

from io import StringIO
from unittest import skip
from ...snescpu.tests.test_statemachine import AbstractTestStateMachine
from ...snescpu.statemachine import StateMachine
from ..disasm import DisassembleStateDQ3

class TestStateMachineDQ3(AbstractTestStateMachine):
    """Tests for disassembling DQ3."""

    game_title = 'DRAGONQUEST3'

    def setUp(self):
        """Prepare the target of testing."""
        self.fsm = StateMachine(
            [DisassembleStateDQ3], 'DisassembleStateDQ3', self.rom)

    def test_disassembled_code(self):
        """Test disassembled code for DQ3."""

        fsm = self.fsm
        fsm.destination = StringIO()
        fsm.run(first=0xC25BA6, last=0xC25BCE)

        output_lines = fsm.destination.getvalue().split('\n')
        self.assertRegex(
            output_lines[0], r'^C2/5BA6:\s+A20000\s+LDX #\$0000$')
        self.assertRegex(
            output_lines[-2], r'^C2/5BCD:\s+60\s+RTS$')
        self.assertEqual(output_lines[-1], '')

    def test_run_brk_operand(self):
        """Test if the operand of the BRK command is 2 bytes."""

        fsm = self.fsm
        fsm.destination = StringIO()

        # People in the Shrine of Dharma.
        fsm.run(first=0xCB9A3E, last=0xCB9A57)

        output_lines = fsm.destination.getvalue().split('\n')

        for i in (0, 2, 4, 6,):
            line = output_lines[i]
            self.assertRegex(
                line, r'^CB/[0-9A-F]{4}:\s+00[0-9A-F]{4}\s+')
            self.assertRegex(
                line, r'BRK #\$[0-9A-F]{4}$')

        self.assertRegex(
            output_lines[-2], r'^CB/9A56:\s+6B\s+RTL$')
        self.assertEqual(output_lines[-1], '')

    @skip('DQ3')
    def test_run_cop_operand(self):
        """Test if the operand of the COP command varies."""
        self.fail('DQ3')
