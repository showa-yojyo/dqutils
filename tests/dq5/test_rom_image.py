"""
Tests for dqutils.snescpu.rom_image.
"""

from dqutils.snescpu.rom_image import get_snes_header

from .. import requires_config


@requires_config
def test_get_snes_header(rom):
    """Test function dqutils.snescpu.rom_image.get_snes_header for DQ5."""

    header = get_snes_header(rom)

    # [offset]: +0 +1 +2 +3 +4 +5 +6 +7 +8 +9 +A +B +C +D +E +F
    # ---------------------------------------------------------
    # 00007FC0: 44 52 41 47 4F 4E 51 55 45 53 54 35 20 20 20 20
    # 00007FD0: 20 20 20 20 20 20 02 0B 03 00 B4 00 06 45 F9 BA
    # 00007FE0: 00 00 00 00 7F 8F 80 8F 7F 8F 5D 88 7F 8F 7F 8F
    # 00007FF0: 00 00 00 00 7F 8F 80 8F 7F 8F 5D 88 39 86 7F 8F

    assert len(header) == 64
    assert header.startswith(b"DRAGONQUEST5")
    assert header[0x1C] ^ header[0x1E] == 0xFF
    assert header[0x1D] ^ header[0x1F] == 0xFF
    assert header[0x15] & 0x01 == 0x00  # LoROM
    assert header[0x17] == 0x0B  # 1.5M => 2M
