#!/usr/bin/env python
"""disasm.py: Disassembler for DRAGONQUEST 6.
"""

from ..snescpu.addressing import get_addressing_mode
from ..snescpu.disasm import disassemble
from ..snescpu.instructions import get_instruction
from ..snescpu.states import (DisassembleState, DumpState)

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

        class JSR(get_instruction(0x22)):
            @staticmethod
            def execute(state, context):
                # TODO: Complete the list of subroutines that
                # take hard-coded argument bytes immediately after
                # JSR operands.
                if self.current_operand == 0xC92AB5:
                    context.update(
                        next_state='DisassembleStateDQ6',
                        byte_count=[1, 2, 3, 2],
                        record_count=1,
                        JSR=True)
                    return context, 'DumpState'
                return context, None

        return {0x00: BRK, 0x02: COP, 0x22: JSR}

if __name__ == '__main__':
    disassemble('DRAGONQUEST6',
                [DisassembleStateDQ6, DumpState],
                'DisassembleStateDQ6')
