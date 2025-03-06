import pytest

from dqutils.dq3.disasm import DisassembleStateDQ3, DumpState
from dqutils.snescpu.rom_image import RomImage

GAME_TITLE = "DRAGONQUEST3"
STATE_CLASSES = (DisassembleStateDQ3, DumpState)
INITIAL_STATE = "DisassembleStateDQ3"


@pytest.fixture
def state_classes():
    """Return the set of state classes for DQ3 disassembler."""
    return STATE_CLASSES


@pytest.fixture
def initial_state():
    """Return the initial state's name of DQ3 disassembler."""
    return INITIAL_STATE


@pytest.fixture
def rom():
    """Return the ROM image supplied to DQ3 disassembler."""
    with RomImage(GAME_TITLE) as retval:
        yield retval
