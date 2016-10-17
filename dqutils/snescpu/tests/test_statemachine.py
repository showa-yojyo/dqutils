"""
Tests for dqutils.snescpu.statemachine.
"""

from unittest import (TestCase, skip)
from io import StringIO
from dqutils.snescpu.rom_image import RomImage
from dqutils.snescpu.statemachine import StateMachine

# pylint: disable=too-many-public-methods
class AbstractTestStateMachine(TestCase):
    """The base class of TestStateMachineDQ classes."""

    game_title = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rom = None
        self.fsm = None

    def run(self, result=None):
        """Run the test."""

        with RomImage(self.game_title) as rom:
            self.rom = rom
            super().run(result)

    def setUp(self):
        """Prepare the target of testing."""
        self.fsm = StateMachine(self.rom)

    def tearDown(self):
        """Clean up."""
        self.fsm = None

    def _do_test_initial(self):
        """Test the initial condition of an object of StateMachine.
        """
        fsm = self.fsm

        self.assertIn(fsm.program_counter, (0x008000, 0xC00000,))
        self.assertIsNotNone(fsm.mapper)
        self.assertIsNone(fsm.current_opcode)
        self.assertIsNone(fsm.current_operand)
        self.assertEqual(fsm.current_operand_size, 0)
        self.assertEqual(fsm.flags, 0)

    def _do_test_until_option(self, first, pattern):
        """This method is used from `test_with_until_option`."""

        fsm = self.fsm
        fsm.destination = StringIO()
        fsm.run(first=first, until_return=True)

        output_lines = fsm.destination.getvalue().split('\n')

        for line in output_lines[:-2]:
            self.assertNotRegex(line, r'(RTI|RTS|RTL)')

        self.assertRegex(output_lines[-2], pattern)
        self.assertEqual(output_lines[-1], '')

# pylint: disable=too-many-public-methods
class TestStateMachineDQ5(AbstractTestStateMachine):
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

# pylint: disable=too-many-public-methods
class TestStateMachineDQ6(AbstractTestStateMachine):
    """Tests for disassembling DQ6."""

    game_title = 'DRAGONQUEST6'

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

# pylint: disable=too-many-public-methods
class TestStateMachineDQ3(AbstractTestStateMachine):
    """Tests for disassembling DQ3."""

    game_title = 'DRAGONQUEST3'

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
