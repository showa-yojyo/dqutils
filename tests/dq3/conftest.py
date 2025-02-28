import pytest

from dqutils.dq3.disasm import DisassembleStateDQ3, DumpState
from dqutils.snescpu.rom_image import RomImage

GAME_TITLE = "DRAGONQUEST3"
STATE_CLASSES = (DisassembleStateDQ3, DumpState)
INITIAL_STATE = "DisassembleStateDQ3"


@pytest.fixture
def state_classes():
    return STATE_CLASSES


@pytest.fixture
def initial_state():
    return INITIAL_STATE


@pytest.fixture
def rom():
    with RomImage(GAME_TITLE) as retval:
        yield retval
