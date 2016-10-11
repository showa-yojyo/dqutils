"""
Provide a state machine for the 65816 Processor.
"""

import sys
from dqutils.snescpu.rom_image import get_snes_header
from dqutils.snescpu.mapper import make_mapper
from dqutils.snescpu.instructions import get_instruction

# Does it need to be configurable?
OUTPUT_FORMAT = '{bank:02X}/{addr:04X}:\t{opcode:02X}{operand_raw:<6}\t{mnemonic} {operand}'

class StateMachine(object):
    """A state machine for the 65816 CPU disassembler."""

    def __init__(self, rom, mapper=None):
        """Initialize an object of class `StateMachine`.

        Parameters
        ----------
        rom : mmap.mmap
            A ROM image object.
        mapper : AbstractMapper, optional
            The mapper to `rom`.
        """

        self.rom = rom
        if mapper:
            self.mapper = mapper
        else:
            self.mapper = make_mapper(header=get_snes_header(rom))

        self.current_opcode = None
        self.current_operand = None
        self.current_operand_size = 0
        self.destination = sys.stdout
        self.flags = 0

    @property
    def program_counter(self):
        """Return the program counter."""
        assert self.rom

        return self.mapper.from_rom(self.rom.tell())

    def run(self, first=0, last=-1, flags=0):
        """Run the state machine on `self.rom`.

        Parameters
        ----------
        first : int, optional, default: 0
            The beginning of the CPU address from which to
            disassemble.
        last : int, optional, default: -1
            The end of the CPU address to which to disassemble.
            If -1 is specified, then disassembling continues
            until the program counter reaches the end of ROM image.
        flags : int, optional, default: 0
            The initial value of the register status bits.
        """

        self.flags = flags
        self.current_opcode = None
        self.current_operand = None
        self.current_operand_size = 0

        self.rom.seek(self.mapper.from_cpu(first))
        if last != -1:
            last_rom_addr = self.mapper.from_cpu(last)
        else:
            last_rom_addr = self.rom.size()

        while self.rom.tell() < last_rom_addr:
            instruction, operand_raw, across_bb = self._read_instruction()
            self._eval_instruction(instruction, across_bb)
            self._print_instruction(instruction, operand_raw, across_bb)

    def _read_instruction(self):
        """Read the current instruction and return as an object."""

        # Read the opcode.
        opcode = self.rom.read(1)
        self.current_opcode = opcode
        instruction = get_instruction(self.current_opcode)

        # Test if PC crossed the bank boundary after the current
        # instraction's opcode has been read.
        if self.program_counter & 0xFFFF == 0x0000:
            self.current_operand_size = 0
            return instruction, '', True

        self.current_operand_size = instruction.actual_operand_size(self)

        # Test if PC crossed the bank boundary after the opcode
        # has been read.
        across_bb = False
        cur_counter = 0xFFFF & self.program_counter
        num_remain_bytes = 0x10000 - cur_counter
        if num_remain_bytes < self.current_operand_size:
            across_bb = True
            self.current_operand_size = num_remain_bytes

        # Read the operand.
        operand_raw = self.rom.read(self.current_operand_size)
        self.current_operand = int.from_bytes(operand_raw, 'little')

        return instruction, operand_raw, across_bb

    def _print_instruction(self, instruction, operand_raw, across_bb):
        """Output disassembled code in one line."""

        # cpu_addr is the value of PC immediately before reading
        # the current opcode.
        addr = self.program_counter - self.current_operand_size - 1
        out = self.destination
        operand_raw = operand_raw.hex().upper() if operand_raw else ''
        mnemonic = instruction.mnemonic if not across_bb else ''
        operand = instruction.format(self) if not across_bb else ''

        print(OUTPUT_FORMAT.format(
            bank=(addr & 0xFF0000) >> 16,
            addr=addr & 0x00FFFF,
            opcode=instruction.opcode,
            operand_raw=operand_raw,
            mnemonic=mnemonic,
            operand=operand).strip(),
              file=out)

    def _eval_instruction(self, instruction, across_bb):
        """Execute the current instruction."""
        if not across_bb:
            instruction.execute(self)
