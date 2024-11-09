#!/usr/bin/env python
"""disasm.py: Disassembler for DRAGONQUEST 3."""

from __future__ import annotations

from typing import TYPE_CHECKING, cast

if TYPE_CHECKING:
    from typing import Final, Self

from dqutils.snescpu.addressing import get_addressing_mode
from dqutils.snescpu.disasm import disassemble
from dqutils.snescpu.instructions import get_instruction
from dqutils.snescpu.states import DisassembleState, DumpState

if TYPE_CHECKING:
    from dqutils.snescpu.instructions import AbstractInstruction, ContextT

# A dictionary of subroutines with following bytes as arguments.
# key: the address of subroutine
# value: the corresponding byte-partition for DumpState.byte_count
# fmt: off
SPECIAL_SUBROUTINES: Final[dict[int, tuple[int, ...]]] = {
    0xC90566: (1, 2, 3, 2, 3,),
    0xC90572: (1, 2, 3, 2, 3,),
    0xC9062D: (1, 2, 3, 2, 3,),
    0xC77808: (2, 2, 2, 2,),
    0xC903E2: (1, 2, 3, 2,),
    0xC903EE: (1, 2, 3, 2,),
    0xC90501: (1, 2, 3, 1,),
    0xC9050D: (1, 2, 3, 1,),
    0xC46F9B: (1, 2, 3,),
    0xC90789: (3, 3,),
    0xC907CC: (3, 3,),
    0xC447D3: (3, 2,),
    0xC44A72: (3, 2,),
    0xC691AD: (3, 2,),
    0xC69234: (3, 2,),
    0xC6928E: (3, 2,),
    0xC908F0: (3, 2,),
    0xC90937: (3, 2,),
    0xC909AE: (3, 2,),
    0xC738E2: (2, 3,),
    0xC04604: (3, 1,),
    0xC2CAD9: (2, 2,),
    0xC2CAE0: (2, 2,),
    0xC2CB2B: (2, 2,),
    0xC2CB32: (2, 2,),
    0xC2CB70: (2, 2,),
    0xC2CB79: (2, 2,),
    0xC2CC25: (2, 2,),
    0xC2CC2C: (2, 2,),
    0xC2CC47: (2, 2,),
    0xC2CC4E: (2, 2,),
    0xC2CC8B: (2, 2,),
    0xC2CC92: (2, 2,),
    0xC2CCF8: (2, 2,),
    0xC42B06: (2, 2,),
    0xC43C07: (3, 1,),
    0xC44739: (3, 1,),
    0xC4487F: (3, 1,),
    0xC44927: (3, 1,),
    0xC4497B: (4,),
    0xC44A03: (3, 1,),
    0xC44BB9: (3, 1,),
    0xC44C1B: (3, 1,),
    0xC44D5E: (4,),
    0xC44DC0: (3, 1,),
    0xC451E2: (3, 1,),
    0xC452E3: (3, 1,),
    0xC77104: (4,),
    0xC77791: (4,),
    0xC027B4: (3,),
    0xC027D8: (3,),
    0xC02ABA: (3,),
    0xC02C2D: (3,),
    0xC02EC7: (3,),
    0xC047B2: (3,),
    0xC04835: (3,),
    0xC32296: (3,),
    0xC3230B: (3,),
    0xC42777: (3,),
    0xC429DA: (3,),
    0xC42A12: (3,),
    0xC42A6D: (3,),
    0xC42DA1: (3,),
    0xC42E19: (3,),
    0xC42E53: (3,),
    0xC42EA9: (3,),
    0xC42ED6: (3,),
    0xC42F5E: (3,),
    0xC42FEB: (3,),
    0xC43041: (3,),
    0xC4307F: (3,),
    0xC43115: (3,),
    0xC43154: (3,),
    0xC43193: (3,),
    0xC431D7: (3,),
    0xC43231: (3,),
    0xC4326F: (3,),
    0xC43305: (3,),
    0xC43337: (3,),
    0xC43376: (3,),
    0xC433BA: (3,),
    0xC43414: (3,),
    0xC43468: (3,),
    0xC4350C: (3,),
    0xC4355D: (3,),
    0xC435A2: (3,),
    0xC43644: (3,),
    0xC43672: (3,),
    0xC4371F: (3,),
    0xC437C1: (3,),
    0xC43808: (3,),
    0xC43859: (3,),
    0xC438FB: (3,),
    0xC43929: (3,),
    0xC439A0: (3,),
    0xC43A42: (3,),
    0xC43AFA: (3,),
    0xC43B5F: (3,),
    0xC43BA6: (3,),
    0xC43F87: (3,),
    0xC446A4: (3,),
    0xC446D6: (3,),
    0xC44708: (3,),
    0xC456BC: (3,),
    0xC45796: (3,),
    0xC457C1: (3,),
    0xC459E4: (3,),
    0xC45A16: (3,),
    0xC45A4A: (3,),
    0xC45A7C: (3,),
    0xC46951: (3,),
    0xC46987: (3,),
    0xC46AFD: (3,),
    0xC773FE: (3,),
    0xC77470: (3,),
    0xC774AA: (3,),
    0xC774E4: (3,),
    0xC77843: (3,),
    0xC77851: (3,),
    0xC7785F: (3,),
    0xC7786D: (3,),
    0xC7787B: (3,),
    0xC77889: (3,),
    0xC77897: (3,),
    0xC778A5: (3,),
    0xC778B3: (3,),
    0xC1A867: (2,),
    0xC1A8D4: (2,),
    0xC1A92E: (2,),
    0xC1A944: (2,),
    0xC1A988: (2,),
    0xC1A9D3: (2,),
    0xC1E32E: (2,),
    0xC1E59C: (2,),
    0xC2CA5B: (2,),
    0xC2CA62: (2,),
    0xC2CA98: (2,),
    0xC2CC03: (2,),
    0xC2CC0A: (2,),
    0xC2CC69: (2,),
    0xC2CC70: (2,),
    0xC3226F: (2,),
    0xC322E4: (2,),
    0xC32359: (2,),
    0xC42763: (2,),
    0xC4297C: (2,),
    0xC42F28: (2,),
    0xC42FAE: (2,),
    0xC43C52: (2,),
    0xC44011: (2,),
    0xC44045: (2,),
    0xC44078: (2,),
    0xC440B0: (2,),
    0xC440F1: (2,),
    0xC44129: (2,),
    0xC44566: (2,),
    0xC445F8: (2,),
    0xC44824: (2,),
    0xC44E32: (2,),
    0xC44E68: (2,),
    0xC44EA6: (2,),
    0xC44FE2: (2,),
    0xC4501B: (2,),
    0xC452AA: (2,),
    0xC455FD: (2,),
    0xC456E7: (2,),
    0xC4691B: (2,),
    0xC46A64: (2,),
    0xC46BED: (2,),
    0xC46C28: (2,),
    0xC73C42: (2,),
    0xC737BE: (2,),
    0xC2BE8A: (1,),
    0xC2C240: (1,),
    0xC2C573: (1,),
    0xC2C739: (1,),
    0xC2C766: (1,),
    0xC2C791: (1,),
    0xC2C7C6: (1,),
    0xC32251: (1,),
    0xC322C6: (1,),
    0xC3233B: (1,),
    0xC323B0: (1,),
    0xC32436: (1,),
    0xC32569: (1,),
    0xC4274F: (1,),
    0xC42B9F: (1,),
    0xC42BCE: (1,),
    0xC42BFD: (1,),
    0xC42C2C: (1,),
    0xC42CF4: (1,),
    0xC42D43: (1,),
    0xC42D72: (1,),
    0xC441AE: (1,),
    0xC44F00: (1,),
    0xC44F55: (1,),
    0xC44FA5: (1,),
    0xC4508A: (1,),
    0xC451A3: (1,),
    0xC45345: (1,),
    0xC45399: (1,),
    0xC453F7: (1,),
    0xC45458: (1,),
    0xC4559E: (1,),
    0xC458C8: (1,),
    0xC45AB0: (1,),
    0xC45ADC: (1,),
    0xC45B1A: (1,),
    0xC45B66: (1,),
    0xC45BEB: (1,),
    0xC45C5A: (1,),
    0xC4624E: (1,),
    0xC463AC: (1,),
    0xC464C9: (1,),
    0xC466EA: (1,),
}
# fmt: on


class DisassembleStateDQ3(DisassembleState):
    """A specialized state."""

    def _init_instructions(self: Self) -> dict[int, type[AbstractInstruction]]:
        immed = get_addressing_mode("Immediate")
        implied = get_addressing_mode("Implied")

        class BRK(get_instruction(0x00)):  # type: ignore[misc]
            operand_size = 3
            addressing_mode = immed

        class COP(get_instruction(0x02)):  # type: ignore[misc]
            operand_size = 1
            addressing_mode = implied

        class JSR(get_instruction(0x22)):  # type: ignore[misc]
            @staticmethod
            def execute(state: DisassembleState, context: ContextT) -> tuple[ContextT, str | None]:  # noqa: ARG004
                addr = cast(int, self.current_operand)
                if byte_count := SPECIAL_SUBROUTINES.get(addr):
                    context.update(
                        next_state="DisassembleStateDQ3",
                        byte_count=byte_count,
                        record_count=1,
                    )
                    return context, "DumpState"
                return context, None

        return {0x00: BRK, 0x02: COP, 0x22: JSR}


if __name__ == "__main__":
    disassemble("DRAGONQUEST3", [DisassembleStateDQ3, DumpState], "DisassembleStateDQ3")
