"""
Tests for dqutils.snescpu.statemachine.
"""

from io import StringIO
from ...snescpu.tests.test_statemachine import AbstractStateMachineTestCase
from ...snescpu.statemachine import StateMachine
from ..disasm import DisassembleStateDQ6

# pylint: disable=too-many-public-methods
class StateMachineTestCase(AbstractStateMachineTestCase):
    """Tests for disassembling DQ6."""

    game_title = 'DRAGONQUEST6'
    state_classes = [DisassembleStateDQ6]
    initial_state = 'DisassembleStateDQ6'

    def test_initial(self):
        """Test the initial condition of StateMachine for DQ6."""
        self._do_test_initial()

    def test_disassembled_code(self):
        """Test disassembled code for DQ6."""

        fsm = self.fsm
        fsm.destination = StringIO()
        fsm.run(first=0xC2B09A, last=0xC2B13F)

        output_lines = fsm.destination.getvalue().split('\n')

        self.assertRegex(
            output_lines[0], r'^C2/B09A:\s+6400\s+STZ \$00$')
        self.assertRegex(
            output_lines[-2], r'^C2/B13E:\s+60\s+RTS$')
        self.assertEqual(output_lines[-1], '')

    def test_run_near_boundary_opcode(self):
        """Test disassembling near boundary (opcode)."""

        fsm = self.fsm
        fsm.destination = StringIO()
        fsm.run(first=0xCAFFFB, last=0xCB0000)

        output_lines = fsm.destination.getvalue().split('\n')

        self.assertRegex(
            output_lines[-2], r'^CA/FFFF:\s+FF$') # !!
        self.assertEqual(output_lines[-1], '')

    def test_run_near_boundary_operand(self):
        """Test disassembling near boundary (operand)."""

        fsm = self.fsm
        fsm.destination = StringIO()
        fsm.run(first=0xCBFFF5, last=0xCC0000)

        output_lines = fsm.destination.getvalue().split('\n')

        self.assertRegex(
            output_lines[-2], r'^CB/FFFD:\s+FFFFFF$') # !!
        self.assertEqual(output_lines[-1], '')

    def test_run_until_return(self):
        """Test disassembling with -u option for the first return
        instruction occurrence.
        """

        self._do_test_until_option(
            0xC2B091, r'^C2/B099:\s+60\s+RTS$')
        self._do_test_until_option(
            0xC2B4AF, r'^C2/B501:\s+6B\s+RTL$')

    def test_run_brk_operand(self):
        """Test if the operand of the BRK command is 2 bytes."""

        fsm = self.fsm
        fsm.destination = StringIO()

        # The information booth in the Slime Arena.
        fsm.run(first=0xC3E601, until_return=True)

        output_lines = fsm.destination.getvalue().split('\n')

        for i in (0, 5, 12,):
            line = output_lines[i]
            self.assertRegex(
                line, r'^C3/E6[0-9A-F]{2}:\s+00[0-9A-F]{2}07\s+')
            self.assertRegex(
                line, r'BRK #\$07[0-9A-F]{2}$')

        self.assertRegex(
            output_lines[-2], r'^C3/E62F:\s+6B\s+RTL$')
        self.assertEqual(output_lines[-1], '')

    def test_run_cop_operand(self):
        """Test if the COP command is 3 bytes long in DQ6."""

        fsm = self.fsm
        fsm.destination = StringIO()

        fsm.run(first=0xCA0029, last=0xCA00AB)
        output_lines = fsm.destination.getvalue().split('\n')
        self.assertRegex(output_lines[0], r'COP #\$[0-9A-F]{6}$')
