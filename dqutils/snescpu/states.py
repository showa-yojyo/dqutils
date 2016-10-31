"""
Provide class State and subclasses.
"""

from abc import ABCMeta
from .instructions import DEFAULT_INSTRUCTIONS

class AbstractState(metaclass=ABCMeta):
    """
    The base class of state subclasses for class `StateMachine`.
    """

    def __init__(self, state_machine):
        """Create an object of class `AbstractState`.

        This class is abstract and cannot be directly instantiated.

        Parameters
        ----------
        state_machine : StateMachine
            The controlling `StateMachine` object.
        """
        self.state_machine = state_machine

    def __call__(self):
        """Do something and return the name of the next state.

        An empty string will be returned to tell that this state is
        the final.

        Returns
        -------
        next_state : str
            The name of the next state for the state machine.
        """
        return ''

    @property
    def program_counter(self):
        """Return the program counter.

        Returns
        -------
        pc : int
        """
        return self.state_machine.program_counter

    def runtime_init(self, **kwargs):
        """Initialize before running the state machine.

        See also
        --------
        `StateMachine.runtime_init`
        """
        pass

    def unlink(self):
        """Remove circular references."""
        self.state_machine = None

# Does it need to be configurable?
OUTPUT_FORMAT = '{bank:02X}/{addr:04X}:\t{opcode:02X}{operand_raw:<6}\t{mnemonic} {operand}'

class DisassembleState(AbstractState):
    """This state provides a disassembler."""

    def __init__(self, state_machine):
        super().__init__(state_machine)
        self.current_opcode = None
        self.current_operand = None
        self.current_operand_size = 0
        self.flags = 0x00
        self.until_return = False

        # Initialize this own instruction table.
        instructions = list(DEFAULT_INSTRUCTIONS)
        overrides = self._init_instructions()
        for opcode, instruction in overrides.items():
            instructions[opcode] = instruction
        self.instructions = instructions

    def __call__(self):
        """Disassemble bytes.

        Returns
        -------
        next_state : str
            The name of the next state for the state machine.
        """

        while not self._is_terminated():
            instruction, operand_raw, across_bb = self._read_instruction()
            self._eval_instruction(instruction, across_bb)
            self._print_instruction(instruction, operand_raw, across_bb)

        return ''

    def runtime_init(self, **kwargs):
        """Initialize before running the state machine.

        Parameters
        ----------
        flags : int, optional, default: 0
            The initial value of the register status bits.
        until_return : bool, optional, default: False
            Immediately terminate processing when RTI, RTS, or RTL
            instruction is processed.

        See also
        --------
        `StateMachine.runtime_init`
        """

        self.current_opcode = None
        self.current_operand = None
        self.current_operand_size = 0
        self.flags = kwargs.get('flags', 0)
        self.until_return = kwargs.get('until_return', False)

    def _is_terminated(self):
        """Determine if this state machine is terminated.

        When --until-return option is enabled,
        detection of the first RTI/RTS/RTL instruction terminates
        the main loop.

        Returns
        -------
        is_terminated : bool
            True if this state machine is to be terminated.
        """

        fsm = self.state_machine
        assert fsm.rom

        if (self.until_return and
            self.current_opcode in (b'\x40', b'\x60', b'\x6B')):
            return True

        return fsm.last_rom_addr <= fsm.rom.tell()

    def _read_instruction(self):
        """Read the current instruction and return as an object."""

        fsm = self.state_machine

        # Read the opcode.
        opcode = fsm.rom.read(1)
        self.current_opcode = opcode
        instruction = self.get_instruction(opcode)

        # Test if PC crossed the bank boundary after the current
        # instraction's opcode has been read.
        if fsm.program_counter & 0xFFFF == 0x0000:
            self.current_operand_size = 0
            return instruction, '', True

        self.current_operand_size = instruction.actual_operand_size(self.flags)

        # Test if PC crossed the bank boundary after the opcode
        # has been read.
        across_bb = False
        cur_counter = 0xFFFF & fsm.program_counter
        num_remain_bytes = 0x10000 - cur_counter
        if num_remain_bytes < self.current_operand_size:
            across_bb = True
            self.current_operand_size = num_remain_bytes

        # Read the operand.
        operand_raw = fsm.rom.read(self.current_operand_size)
        self.current_operand = int.from_bytes(operand_raw, 'little')

        return instruction, operand_raw, across_bb

    def _eval_instruction(self, instruction, across_bb):
        """Execute the current instruction.

        Returns
        -------
        instruction : AbstractInstruction
            The instruction to be output to `self.destination`.
        operand_raw : bytes
            The unprocessed operand bytes in the ROM image.
        across_bb : bool
            True if this line goes across the PB boundary.
        """
        if not across_bb:
            instruction.execute(self)

    def _print_instruction(self, instruction, operand_raw, across_bb):
        """Output disassembled code in one line.

        Parameters
        ----------
        instruction : AbstractInstruction
            The instruction to be output to `self.destination`.
        operand_raw : bytes
            The unprocessed operand bytes in the ROM image.
        across_bb : bool
            True if this line goes across the PB boundary.
        """

        fsm = self.state_machine

        # cpu_addr is the value of PC immediately before reading
        # the current opcode.
        addr = fsm.program_counter - self.current_operand_size - 1
        out = fsm.destination
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

    def _init_instructions(self):
        """Return specialized instructions.

        Override this method if necessary, especially for BRK, COP,
        JSR commands.

        Returns
        -------
        instructions : dict
            A dictionary with integer keys i.e. operand  whose
            values are specialization of class `AbstractInstruction`.
        """

        return {}

    def get_instruction(self, opcode):
        """Return an object of class `AbstractInstruction`.

        Parameters
        ----------
        opcode : bytes
            A 1 byte value.

        Returns
        -------
        instruction : AbstractInstruction
            An object for one of instruction of the 65816 Processor.
        """

        if isinstance(opcode, bytes):
            opcode = int.from_bytes(opcode, 'little')

        return self.instructions[opcode]

FORMAT_STRING = '{:02X}/{:04X}:\t{}'

class DumpState(AbstractState):
    """This state provides `hexdump`."""

    def __init__(self, state_machine):
        super().__init__(state_machine)
        self.byte_count = 0
        self.record_count = 0

    def __call__(self):
        """
        Perform byte-by-byte dump the contents of a ROM, in
        hexadecimal format.

        Returns
        -------
        next_state : str
            The name of the next state for the state machine.
        """

        fsm = self.state_machine
        rom = fsm.rom
        out = fsm.destination
        while fsm.rom.tell() < fsm.last_rom_addr:
            cpu_address = fsm.program_counter
            bank = (cpu_address & 0xFF0000) >> 16
            offset = cpu_address & 0x00FFFF
            if offset + self.byte_count > 0x10000:
                data = rom.read(0x10000 - offset)
            else:
                data = rom.read(self.byte_count)

            print(FORMAT_STRING.format(
                bank, offset, data.hex().upper()),
                  file=out)

        return ''

    def runtime_init(self, **kwargs):
        """Initialize before running the state machine.

        Parameters
        ----------
        flags : int, optional, default: 0
            The initial value of the register status bits.
        until_return : bool, optional, default: False
            Immediately terminate processing when RTI, RTS, or RTL
            instruction is processed.

        See also
        --------
        `StateMachine.runtime_init`
        """

        self.byte_count = kwargs.get('byte_count', 0)
        self.record_count = kwargs.get('record_count', 0)
