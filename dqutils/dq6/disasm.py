#!/usr/bin/env python
"""disasm.py: Disassembler for DRAGONQUEST 6.
"""

from ..snescpu.addressing import get_addressing_mode
from ..snescpu.disasm import disassemble
from ..snescpu.instructions import get_instruction
from ..snescpu.states import (DisassembleState, DumpState)

# TODO: Complete the list of subroutines that
# take hard-coded argument bytes immediately after
# JSR operands.

# A dictionary of subroutines with following bytes as arguments.
# key: the address of subroutine
# value: the corresponding byte-partition for DumpState.byte_count
SPECIAL_SUBROUTINES = {
    0xC92C2D: (1, 2, 3, 2, 3,),
    0xC92C39: (1, 2, 3, 2, 3,),
    0xC92CE8: (1, 2, 3, 2, 3,),
    0xC92CF4: (1, 2, 3, 2, 3,),
    0xC92AA9: (1, 2, 3, 2,),
    0xC92AB5: (1, 2, 3, 2,),
    0xC92B41: (1, 2, 3, 2,),
    0xC92B4D: (1, 2, 3, 2,),
    0xC47CA6: (2, 3, 2,),
    0xC92BC8: (1, 2, 3, 1,),
    0xC92BD4: (1, 2, 3, 1,),
    0xC47B39: (3, 3,),
    0xC92E50: (3, 3,),
    0xC92E93: (3, 3,),
    0xC92F6B: (3, 3,),
    0xC92FB7: (3, 2,),
    0xC93009: (3, 2,),
    0xC93086: (3, 2,),
    0xC2EFA7: (2, 2,),
    0xC2EFAE: (2, 2,),
    0xC2EFF4: (2, 2,),
    0xC2EFFB: (2, 2,),
    0xC2F034: (2, 2,),
    0xC2F03D: (2, 2,),
    0xC2F0DF: (2, 2,),
    0xC2F0E6: (2, 2,),
    0xC2F0FC: (2, 2,),
    0xC2F103: (2, 2,),
    0xC2F136: (2, 2,),
    0xC2F13D: (2, 2,),
    0xC2F212: (2, 2,),
    0xC2F27E: (2, 2,),
    0xC42E6E: (2, 2,),
    0xC42FC9: (2, 2,),
    0xC45790: (2, 2,),
    0xC07C8A: (4,),
    0xC42E1F: (4,),
    0xC44065: (4,),
    0xC451BA: (4,),
    0xC45217: (4,),
    0xC452E5: (4,),
    0xC4535C: (4,),
    0xC022CF: (3,),
    0xC022FA: (3,),
    0xC07E20: (3,),
    0xC07E7B: (3,),
    0xC1F649: (3,),
    0xC42C26: (3,),
    0xC42DB2: (3,),
    0xC43061: (3,),
    0xC43641: (3,),
    0xC438A3: (3,),
    0xC4391D: (3,),
    0xC43960: (3,),
    0xC43B76: (3,),
    0xC43F5D: (3,),
    0xC43FAC: (3,),
    0xC43FFB: (3,),
    0xC4461E: (3,),
    0xC44651: (3,),
    0xC44685: (3,),
    0xC446DA: (3,),
    0xC44729: (3,),
    0xC4475C: (3,),
    0xC447BD: (3,),
    0xC447F0: (3,),
    0xC44823: (3,),
    0xC44864: (3,),
    0xC448AF: (3,),
    0xC448E2: (3,),
    0xC4494E: (3,),
    0xC44996: (3,),
    0xC449C9: (3,),
    0xC44A30: (3,),
    0xC44A63: (3,),
    0xC44ACB: (3,),
    0xC44AFE: (3,),
    0xC44B65: (3,),
    0xC44B98: (3,),
    0xC44C04: (3,),
    0xC44C37: (3,),
    0xC44CA3: (3,),
    0xC44FA1: (3,),
    0xC4504C: (3,),
    0xC450F1: (3,),
    0xC45124: (3,),
    0xC45157: (3,),
    0xC45294: (3,),
    0xC455E7: (3,),
    0xC4562D: (3,),
    0xC4572B: (3,),
    0xC458BC: (3,),
    0xC45941: (3,),
    0xC459C6: (3,),
    0xC45A7E: (3,),
    0xC45B66: (3,),
    0xC45BA2: (3,),
    0xC45BD1: (3,),
    0xC45CBA: (3,),
    0xC49079: (3,),
    0xC02A16: (2,),
    0xC1F32A: (2,),
    0xC1F598: (2,),
    0xC1F602: (2,),
    0xC2EF33: (2,),
    0xC2EF3A: (2,),
    0xC2EF6B: (2,),
    0xC2EF74: (2,),
    0xC2F0C2: (2,),
    0xC2F0C9: (2,),
    0xC2F119: (2,),
    0xC2F120: (2,),
    0xC42B1C: (2,),
    0xC434D8: (2,),
    0xC43674: (2,),
    0xC439D0: (2,),
    0xC43C0B: (2,),
    0xC43C54: (2,),
    0xC43D74: (2,),
    0xC43E13: (2,),
    0xC441C2: (2,),
    0xC44D34: (2,),
    0xC44D81: (2,),
    0xC44DD4: (2,),
    0xC44E2B: (2,),
    0xC44F58: (2,),
    0xC450A4: (2,),
    0xC45D7A: (2,),
    0xC45DAF: (2,),
    0xC45DE4: (2,),
    0xC45E19: (2,),
    0xC45E4E: (2,),
    0xC45E83: (2,),
    0xC45EB8: (2,),
    0xC45EEC: (2,),
    0xC45F3C: (2,),
    0xC461CC: (2,),
    0xC59977: (2,),
    0xC2E4DC: (1,),
    0xC2E7DB: (1,),
    0xC2E939: (1,),
    0xC2E966: (1,),
    0xC2E991: (1,),
    0xC2E9C6: (1,),
    0xC427E0: (1,),
    0xC42808: (1,),
    0xC42862: (1,),
    0xC42895: (1,),
    0xC429E3: (1,),
    0xC42AA1: (1,),
    0xC42FDC: (1,),
    0xC43488: (1,),
    0xC434B2: (1,),
    0xC43513: (1,),
    0xC4353B: (1,),
    0xC4358C: (1,),
    0xC435FC: (1,),
    0xC43F05: (1,),
    0xC4584C: (1,),
    0xC461FA: (1,),
    0xC46612: (1,),
    0xC466FE: (1,),}

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
                addr = self.current_operand
                byte_count = SPECIAL_SUBROUTINES.get(addr)
                if byte_count:
                    context.update(
                        next_state='DisassembleStateDQ6',
                        byte_count=byte_count,
                        record_count=1,
                        JSR=True)
                    return context, 'DumpState'
                return context, None

        return {0x00: BRK, 0x02: COP, 0x22: JSR}

if __name__ == '__main__':
    disassemble('DRAGONQUEST6',
                [DisassembleStateDQ6, DumpState],
                'DisassembleStateDQ6')
