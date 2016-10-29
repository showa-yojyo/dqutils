#!/usr/bin/env python
"""disasm.py: Disassembler for DRAGONQUEST 6.
"""

from ..snescpu.cui import main
from ..snescpu.addressing import get_addressing_mode
from ..snescpu.instructions import get_instruction
from ..snescpu.states import DisassembleState

class DisassembleStateDQ6(DisassembleState):
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
    main('DRAGONQUEST6',
         [DisassembleStateDQ6], 'DisassembleStateDQ6')
