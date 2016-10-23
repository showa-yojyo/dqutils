"""
Tests for dqutils.snescpu.statemachine.
"""

from unittest import TestCase
from io import StringIO
from dqutils.snescpu.rom_image import RomImage
from dqutils.snescpu.statemachine import StateMachine

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
