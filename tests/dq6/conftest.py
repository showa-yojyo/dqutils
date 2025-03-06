import pytest

from dqutils.dq6.disasm import DisassembleStateDQ6, DumpState
from dqutils.snescpu.rom_image import RomImage

GAME_TITLE = "DRAGONQUEST6"
STATE_CLASSES = (DisassembleStateDQ6, DumpState)
INITIAL_STATE = "DisassembleStateDQ6"


@pytest.fixture
def state_classes():
    """Return the set of state classes for DQ6 disassembler."""
    return STATE_CLASSES


@pytest.fixture
def initial_state():
    """Return the initial state's name of DQ6 disassembler."""
    return INITIAL_STATE


@pytest.fixture
def rom():
    """Return the ROM image supplied to DQ6 disassembler."""
    with RomImage(GAME_TITLE) as retval:
        yield retval
