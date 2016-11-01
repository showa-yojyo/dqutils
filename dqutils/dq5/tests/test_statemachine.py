"""
Tests for dqutils.snescpu.statemachine.
"""

from io import StringIO
from unittest import skip
from ...snescpu.tests.test_statemachine import AbstractStateMachineTestCase

class StateMachineTestCase(AbstractStateMachineTestCase):
    """Tests for class dqutils.snescpu.statemachine.StateMachine."""

    game_title = 'DRAGONQUEST5'

    def test_initial(self):
        """Test the initial condition of StateMachine for DQ5."""
        self._do_test_initial()

    def test_disassembled_code(self):
        """Test disassembled code for DQ5."""

        fsm = self.fsm
        fsm.destination = StringIO()
        fsm.run(first=0x23E1FE, last=0x23E24C)

        output_lines = fsm.destination.getvalue().split('\n')

        self.assertRegex(output_lines[0], r'^23/E1FE:\s+08\s+PHP$')
        self.assertRegex(output_lines[-2], r'^23/E24B:\s+6B\s+RTL$')
        self.assertEqual(output_lines[-1], '')

    def test_run_until_return(self):
        """Test disassembling with -u option for the first return
        instruction occurrence.
        """

        self._do_test_until_option(
            0x008F80, r'^00/8FAB:\s+40\s+RTI$')

    @skip('DQ5')
    def test_run_brk_operand(self):
        """Test if the operand of the BRK command varies."""
        self.fail('DQ5')

    @skip('DQ5')
    def test_run_cop_operand(self):
        """Test if the operand of the COP command varies."""
        self.fail('DQ5')
