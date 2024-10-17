"""
Tests for dqutils.snescpu.disasm.
"""

from unittest import TestCase
from unittest.mock import Mock
from ...snescpu.disasm import create_args
from ...snescpu.rom_image import RomImage
from ..disasm import DisassembleStateDQ6

class DisasmTestCase(TestCase):
    """Tests dqutils.snescpu.disasm for DQ6."""

    def test_create_args_default(self):
        """Test create_args for DQ6 default values."""

        with RomImage('DRAGONQUEST6') as rom:
            args, _ = create_args(rom, [])

            self.assertEqual(args['flags'], 0)
            self.assertEqual(args['first'], 0xC00000)
            self.assertEqual(args['last'], -1)
            self.assertFalse(args['until_return'])

    def test_specialized_state(self):
        """Test class `DisassembleStateDQ6`."""

        fsm = Mock(program_counter='dummy')
        state = DisassembleStateDQ6(fsm)
        state.runtime_init()

        brk = state.get_instruction(0x00)
        self.assertEqual(brk.operand_size, 3)

        cop = state.get_instruction(0x02)
        self.assertEqual(cop.operand_size, 1)
