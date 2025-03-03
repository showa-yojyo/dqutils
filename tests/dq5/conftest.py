import pytest

from dqutils.dq5.disasm import DisassembleStateDQ5, DumpState
from dqutils.snescpu.rom_image import RomImage

GAME_TITLE = "DRAGONQUEST5"
STATE_CLASSES = (DisassembleStateDQ5, DumpState)
INITIAL_STATE = "DisassembleStateDQ5"


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
