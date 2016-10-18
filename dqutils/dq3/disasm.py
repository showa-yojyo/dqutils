#!/usr/bin/env python
"""disasm.py: Disassembler for DRAGONQUEST 3.
"""

from dqutils.snescpu.cui import main
from dqutils.snescpu.addressing import get_addressing_mode
from dqutils.snescpu.instructions import get_instruction
from dqutils.snescpu.statemachine import StateMachine

class StateMachineDQ3(StateMachine):
    """A specialized state machine."""

    def init_instructions(self):
        immed = get_addressing_mode('Immediate')
        class BRK(get_instruction(0x00)):
            operand_size = 3
            addressing_mode = immed

        class COP(get_instruction(0x02)):
            operand_size = 4
            addressing_mode = immed

        return {0x00: BRK, 0x02: COP}

if __name__ == '__main__':
    main('DRAGONQUEST3', StateMachineDQ3)
