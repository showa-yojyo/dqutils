#!/usr/bin/env python
"""disasm.py: Disassembler for DRAGONQUEST 5.
"""

from ..snescpu.cui import main
from ..snescpu.states import DisassembleState

if __name__ == '__main__':
    main('DRAGONQUEST5', [DisassembleState], 'DisassembleState')
