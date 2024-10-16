#!/usr/bin/env python
"""disasm.py: Disassembler for DRAGONQUEST 5.
"""

from ..snescpu.disasm import disassemble
from ..snescpu.instructions import get_instruction
from ..snescpu.states import (DisassembleState, DumpState)

BRK_BPL = (
    (0,),
    (0,), # BRK #$01
    (0,), # BRK #$02
    (0,), # BRK #$03
    (2,), # BRK #$04
    (3,), # BRK #$05
    (0,), # BRK #$06
    (1,), # BRK #$07
    (0,), # BRK #$08
    (1,), # BRK #$09
    (2,), # BRK #$0A
    (2,), # BRK #$0B
    (2,), # BRK #$0C
    (2,), # BRK #$0D
    (0,), # BRK #$0E
    (1,), # BRK #$0F
    (1,), # BRK #$10
    (1,), # BRK #$11
    (1,), # BRK #$12
    (1,), # BRK #$13
    (2,), # BRK #$14
    (2,), # BRK #$15
    (2,), # BRK #$16
    (2,), # BRK #$17
    (2,), # BRK #$18
    (2,), # BRK #$19
    (0,),)# BRK #$1A

BRK_BMI = (
    (0,), # BRK #$80
    (1,), # BRK #$81
    (0,), # BRK #$82
    (1,), # BRK #$83
    (0,), # BRK #$84
    (1,), # BRK #$85
    (0,), # BRK #$86
    (1,), # BRK #$87
    (1,), # BRK #$88
    (2,), # BRK #$89
    (1,), # BRK #$8A
    (2,), # BRK #$8B
    (1,), # BRK #$8C
    (2,), # BRK #$8D
    (1,), # BRK #$8E
    (2,), # BRK #$8F
    (2,), # BRK #$90
    (2,), # BRK #$91
    (2,), # BRK #$92
    (3,), # BRK #$93
    (1,), # BRK #$94
    (1,), # BRK #$95
    (1,), # BRK #$96
    (1,), # BRK #$97
    (1,), # BRK #$98
    (1,), # BRK #$99
    (1,), # BRK #$9A
    (1,), # BRK #$9B
    (1,), # BRK #$9C
    (1,), # BRK #$9D
    (1,), # BRK #$9E
    (1,), # BRK #$9F
    (1,), # BRK #$A0
    (1,), # BRK #$A1
    (1,), # BRK #$A2
    (1,), # BRK #$A3
    (1,), # BRK #$A4
    (1,), # BRK #$A5
    (1,), # BRK #$A6
    (1,), # BRK #$A7
    (1,), # BRK #$A8
    (1,), # BRK #$A9
    (0,), # BRK #$AA
    (1,), # BRK #$AB
    (1,),)# BRK #$AC

class DisassembleStateDQ5(DisassembleState):
    """A specialized state class for disassembling DQ5."""

    def _init_instructions(self):
        class BRK(get_instruction(0x00)):
            @staticmethod
            def execute(state, context):
                sigbyte = self.current_operand
                if sigbyte == 0x00 or 0xAD <= sigbyte:
                    return context, None
                elif sigbyte < 0x1B:
                    byte_count = BRK_BPL[sigbyte]
                elif 0x1B <= sigbyte < 0x80:
                    # This case is illegal.
                    return context, None
                else:
                    byte_count = BRK_BMI[sigbyte - 0x80]

                if byte_count == (0,):
                    return context, None

                context.update(
                    next_state='DisassembleStateDQ5',
                    byte_count=byte_count,
                    record_count=1,)

                return context, 'DumpState'

        return {0x00: BRK}

if __name__ == '__main__':
    disassemble('DRAGONQUEST5',
                [DisassembleStateDQ5, DumpState],
                'DisassembleStateDQ5')
