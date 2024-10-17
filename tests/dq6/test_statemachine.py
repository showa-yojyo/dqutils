"""
Tests for dqutils.snescpu.statemachine.
"""

from io import StringIO
from dqutils.dq6.disasm import (DisassembleStateDQ6, DumpState)
from ..snescpu.test_statemachine import AbstractStateMachineTestCase

# pylint: disable=too-many-public-methods
class StateMachineTestCase(AbstractStateMachineTestCase):
    """Tests for disassembling DQ6."""

    game_title = 'DRAGONQUEST6'
    state_classes = [DisassembleStateDQ6, DumpState]
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

    def test_run_near_boundary_opcode(self):
        """Test disassembling near boundary (opcode)."""

        fsm = self.fsm
        fsm.destination = StringIO()
        fsm.run(first=0xCEFFFD, until_return=True)

        output_lines = fsm.destination.getvalue().split('\n')

        self.assertRegex(
            output_lines[-2], r'^CE/FFFF:\s+6B\s+RTL$')
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
        """Test if the COP command has no operands in DQ6."""

        fsm = self.fsm
        fsm.destination = StringIO()

        fsm.run(first=0xCA0029, last=0xCA00AB)
        output_lines = fsm.destination.getvalue().split('\n')
        self.assertRegex(output_lines[0], r'^CA/0029:\t02\s+COP$')
        self.assertRegex(output_lines[1], r'^CA/002A:\t4C1E00\s+JMP \$001E$')

    def test_jsr_args(self):
        """Test outputs of JSR instructions that have arguments."""

        fsm = self.fsm
        fsm.destination = StringIO()

        # JSR $C92AB5 (RTL+8)
        fsm.run(first=0xC37D14, until_return=True)
        results = fsm.destination.getvalue().split('\n')

        HEX_RE = r'[0-9A-F]'

        self.assertEqual(
            results[0], 'C3/7D14:\t22B52AC9\tJSR $C92AB5')
        self.assertRegex(
            results[1], '^C3/7D18:\t' + HEX_RE + '{2}$')
        self.assertRegex(
            results[2], '^C3/7D19:\t' + HEX_RE + '{4}$')
        self.assertRegex(
            results[3], '^C3/7D1B:\t' + HEX_RE + '{6}$')
        self.assertRegex(
            results[4], '^C3/7D1E:\t' + HEX_RE + '{4}$')
        self.assertEqual(
            results[5], 'C3/7D20:\t8D8C38  \tSTA $388C')
