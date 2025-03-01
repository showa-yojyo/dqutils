import pytest

from dqutils.dq6.disasm import DisassembleStateDQ6, DumpState
from dqutils.snescpu.rom_image import RomImage

GAME_TITLE = "DRAGONQUEST6"
STATE_CLASSES = (DisassembleStateDQ6, DumpState)
INITIAL_STATE = "DisassembleStateDQ6"


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
