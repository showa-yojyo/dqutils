"""
Tests for dqutils.snescpu.states.
"""

from unittest import TestCase
from unittest.mock import Mock
from dqutils.snescpu.instructions import DEFAULT_INSTRUCTIONS
from dqutils.snescpu.states import DisassembleState, DumpState


class DisassembleStateTestCase(TestCase):
    """A TestCase for class DisassembleState."""

    def test_initial_properties(self):
        """
        Test the initial condition of an object of class
        `DisassembleState`.
        """

        fsm = Mock(program_counter="dummy")
        state = DisassembleState(fsm)
        self.assertEqual(state.state_machine, fsm)
        self.assertIsNone(state.current_opcode)
        self.assertIsNone(state.current_operand)
        self.assertEqual(state.current_operand_size, 0)
        self.assertEqual(state.flags, 0)
        self.assertFalse(state.until_return)
        self.assertSequenceEqual(state.instructions, DEFAULT_INSTRUCTIONS)

    def test_runtime_init(self):
        """
        Test behaviors of `DisassembleState.runtime_init`.
        """

        fsm = Mock(program_counter="dummy")
        state = DisassembleState(fsm)

        # The default behavior.
        state.runtime_init()
        self.assertIsNone(state.current_opcode)
        self.assertIsNone(state.current_operand)
        self.assertEqual(state.current_operand_size, 0)
        self.assertEqual(state.flags, 0)
        self.assertFalse(state.until_return)

        # Specify some keyword arguments.
        state.runtime_init(flags=0x30, until_return=True)
        self.assertEqual(state.flags, 0x30)
        self.assertTrue(state.until_return)

    def test_get_instruction(self):
        """
        Test behaviors of `DisassembleState.get_instruction`.
        """

        fsm = Mock(program_counter="dummy")
        state = DisassembleState(fsm)
        state.runtime_init()

        self.assertEqual(state.get_instruction(0x00), DEFAULT_INSTRUCTIONS[0])
        self.assertEqual(state.get_instruction(b"\x03"), DEFAULT_INSTRUCTIONS[3])


class DumpStateTestCase(TestCase):
    """Test class DumpState."""

    def test_initial_properties(self):
        """
        Test the initial condition of an object of class
        `DumpState`.
        """

        fsm = Mock(program_counter="dummy")
        state = DumpState(fsm)
        self.assertEqual(state.state_machine, fsm)
        self.assertEqual(state.byte_count, ())
        self.assertEqual(state.record_count, 0)

    def test_runtime_init(self):
        """
        Test behavior of `DumpState.runtime_init`.
        """

        fsm = Mock(program_counter="dummy")
        state = DumpState(fsm)
        state.runtime_init(byte_count=[20], record_count=47894)
        self.assertEqual(state.byte_count, [20])
        self.assertEqual(state.record_count, 47894)

        state.runtime_init()
        self.assertEqual(state.byte_count, ())
        self.assertEqual(state.record_count, 0)
