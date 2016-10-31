#!/usr/bin/env python
"""disasm.py: Disassembler for DRAGONQUEST 3.
"""

from ..snescpu.addressing import get_addressing_mode
from ..snescpu.disasm import disassemble
from ..snescpu.instructions import get_instruction
from ..snescpu.states import DisassembleState

class DisassembleStateDQ3(DisassembleState):
    """A specialized state."""

    def _init_instructions(self):
        immed = get_addressing_mode('Immediate')
        class BRK(get_instruction(0x00)):
            operand_size = 3
            addressing_mode = immed

        class COP(get_instruction(0x02)):
            operand_size = 4
            addressing_mode = immed

        return {0x00: BRK, 0x02: COP}

if __name__ == '__main__':
    disassemble('DRAGONQUEST3',
         [DisassembleStateDQ3], 'DisassembleStateDQ3')
