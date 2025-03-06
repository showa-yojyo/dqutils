import pytest

from dqutils.dq5.disasm import DisassembleStateDQ5, DumpState
from dqutils.snescpu.rom_image import RomImage

GAME_TITLE = "DRAGONQUEST5"
STATE_CLASSES = (DisassembleStateDQ5, DumpState)
INITIAL_STATE = "DisassembleStateDQ5"


@pytest.fixture
def state_classes():
    """Return the set of state classes for DQ5 disassembler."""
    return STATE_CLASSES


@pytest.fixture
def initial_state():
    """Return the initial state's name of DQ5 disassembler."""
    return INITIAL_STATE


@pytest.fixture
def rom():
    """Return the ROM image supplied to DQ5 disassembler."""
    with RomImage(GAME_TITLE) as retval:
        yield retval
