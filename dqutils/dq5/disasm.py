#!/usr/bin/env python
"""disasm.py: Disassembler for DRAGONQUEST 5.
"""

from ..snescpu.disasm import disassemble
from ..snescpu.states import DisassembleState

if __name__ == '__main__':
    disassemble(
        'DRAGONQUEST5', [DisassembleState], 'DisassembleState')
