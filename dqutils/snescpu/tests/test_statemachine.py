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

    @skip
    def do_test_initial(self):
        """Test the initial condition of an object of StateMachine."""
        fsm = self.fsm

        self.assertEqual(fsm.program_counter, 0)
        self.assertIsNotNone(fsm.mapper)
        self.assertIsNone(fsm.current_opcode)
        self.assertIsNone(fsm.current_operand)
        self.assertEqual(fsm.current_operand_size, 0)
        self.assertEqual(fsm.flags, 0)

# pylint: disable=too-many-public-methods
class TestStateMachineDQ5(AbstractTestStateMachine):
    """Tests for class dqutils.snescpu.statemachine.StateMachine."""

    game_title = 'DRAGONQUEST5'

    def test_initial(self):
        """Test the initial condition of an object of StateMachine."""
        self.do_test_initial()

    def test_disassembled_code(self):
        """Test disassembled code for DQ5."""

        fsm = self.fsm
        fsm.destination = StringIO()
        fsm.run(first=0x23E1FE, last=0x23E24C)

        output_lines = fsm.destination.getvalue().split('\n')

        outfs = output_lines[0].split()
        self.assertEqual(outfs[0], '23/E1FE:')
        self.assertEqual(outfs[1], '08')
        self.assertEqual(outfs[2], 'PHP')

        self.assertEqual(output_lines[-1], '')

        outps = output_lines[-2].split()
        self.assertEqual(outps[0], '23/E24B:')
        self.assertEqual(outps[1], '6B')
        self.assertEqual(outps[2], 'RTL')

# pylint: disable=too-many-public-methods
class TestStateMachineDQ6(AbstractTestStateMachine):
    """Tests for disassembling DQ6."""

    game_title = 'DRAGONQUEST6'

    def test_disassembled_code(self):
        """Test disassembled code for DQ6."""

        fsm = self.fsm
        fsm.destination = StringIO()
        fsm.run(first=0xC2B09A, last=0xC2B13F)

        output_lines = fsm.destination.getvalue().split('\n')

        outfs = output_lines[0].split()
        self.assertEqual(outfs[0], 'C2/B09A:')
        self.assertEqual(outfs[1], '6400')
        self.assertEqual(outfs[2], 'STZ')
        self.assertEqual(outfs[3], '$00')

        self.assertEqual(output_lines[-1], '')

        outps = output_lines[-2].split()
        self.assertEqual(outps[0], 'C2/B13E:')
        self.assertEqual(outps[1], '60')
        self.assertEqual(outps[2], 'RTS')

    def test_run_near_boundary_opcode(self):
        """Test disassembling near boundary (opcode)."""

        fsm = self.fsm
        fsm.destination = StringIO()
        fsm.run(first=0xCAFFFB, last=0xCB0000)

        output_lines = fsm.destination.getvalue().split('\n')

        self.assertEqual(output_lines[-1], '')

        outps = output_lines[-2].split()
        self.assertEqual(outps[0], 'CA/FFFF:')
        self.assertEqual(outps[1], 'FF') # !!

    def test_run_near_boundary_operand(self):
        """Test disassembling near boundary (operand)."""

        fsm = self.fsm
        fsm.destination = StringIO()
        fsm.run(first=0xCBFFF5, last=0xCC0000)

        output_lines = fsm.destination.getvalue().split('\n')

        self.assertEqual(output_lines[-1], '')

        outps = output_lines[-2].split()
        self.assertEqual(outps[0], 'CB/FFFD:')
        self.assertEqual(outps[1], 'FFFFFF') # !!

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

        outfs = output_lines[0].split()
        self.assertEqual(outfs[0], 'C2/5BA6:')
        self.assertEqual(outfs[1], 'A20000')
        self.assertEqual(outfs[2], 'LDX')
        self.assertEqual(outfs[3], '#$0000')

        self.assertEqual(output_lines[-1], '')

        outps = output_lines[-2].split()
        self.assertEqual(outps[0], 'C2/5BCD:')
        self.assertEqual(outps[1], '60')
        self.assertEqual(outps[2], 'RTS')
