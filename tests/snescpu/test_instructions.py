"""
Tests for dqutils.snescpu.instructions.
"""

from unittest import TestCase
from unittest.mock import Mock

from dqutils.snescpu.instructions import INSTRUCTION_TABLE, get_instruction


# pylint: disable=too-many-public-methods
class InstructionsTestCase(TestCase):
    """Tests for dqutils.snescpu.instructions."""

    def test_get_instruction(self):
        """Test get_instruction."""

        for i, item in enumerate(INSTRUCTION_TABLE):
            inst = get_instruction(i)
            self.assertEqual(inst.opcode, i)
            self.assertTrue(inst.mnemonic.upper())
            self.assertEqual(inst.mnemonic, item[0].upper())
            self.assertEqual(inst.operand_size, item[2])

    def test_invalid_instruction(self):
        """Test get_instruction for invalid opcode."""

        self.assertRaises(IndexError, get_instruction, 666)

    def test_instruction_rep(self):
        """Test REP."""

        inst = get_instruction(0xC2)
        self.assertEqual(inst.mnemonic, "REP")

        fsm = Mock(flags=0xFF, current_operand=0x30)
        inst.execute(fsm, None)
        self.assertEqual(fsm.flags & 0x30, 0)

        fsm = Mock(flags=0xFF, current_operand=0x00)
        inst.execute(fsm, None)
        self.assertEqual(fsm.flags, 0xFF)

    def test_instruction_sep(self):
        """Test SEP."""

        inst = get_instruction(0xE2)
        self.assertEqual(inst.mnemonic, "SEP")

        fsm = Mock(flags=0xFF, current_operand=0x30)
        inst.execute(fsm, None)
        self.assertEqual(fsm.flags, 0xFF)

        fsm = Mock(flags=0x00, current_operand=0x30)
        inst.execute(fsm, None)
        self.assertEqual(fsm.flags, 0x30)
