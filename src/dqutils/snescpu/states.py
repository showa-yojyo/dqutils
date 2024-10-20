"""
Provide class State and subclasses.
"""

from __future__ import annotations

from abc import ABCMeta
from itertools import (chain, repeat)
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import MutableMapping
    from typing import Any, Sequence, Self, TypeAlias
    ContextT: TypeAlias = MutableMapping[str, Any]

from .instructions import DEFAULT_INSTRUCTIONS
if TYPE_CHECKING:
    from .instructions import AbstractInstruction
    from .statemachine import StateMachine

class AbstractState(metaclass=ABCMeta):
    """
    The base class of state subclasses for class `StateMachine`.
    """

    def __init__(self: Self, state_machine: StateMachine) -> None:
        """Create an object of class `AbstractState`.

        This class is abstract and cannot be directly instantiated.

        Parameters
        ----------
        state_machine : StateMachine
            The controlling `StateMachine` object.

        Postconditions
        --------------
        >>> self.state_machine is state_machine
        """
        self.state_machine: StateMachine | None = state_machine

    def __call__(self: Self, context: ContextT) -> tuple[ContextT, str|None]:
        """Do something and return the name of the next state.

        An empty string will be returned to tell that this state is
        the final.

        Parameters
        ----------
        context : dict
            Depends on your application.

        Returns
        -------
        context : dict
            Depends on your application.
        next_state : str
            The name of the next state for the state machine.
        """
        return context, None

    @property
    def program_counter(self: Self) -> int:
        """Return the program counter.

        Returns
        -------
        pc : int
        """
        assert self.state_machine
        return self.state_machine.program_counter

    def runtime_init(self: Self, **kwargs) -> None:
        """Initialize before running the state machine.

        See also
        --------
        `StateMachine.runtime_init`
        """
        pass

    def unlink(self: Self) -> None:
        """Remove circular references.

        Postconditions
        --------------
        >>> self.state_machine is None
        """
        self.state_machine = None

# Does it need to be configurable?
OUTPUT_FORMAT = ('{bank:02X}/{addr:04X}:\t'
                 '{opcode:02X}{operand_raw:<6}\t'
                 '{mnemonic} {operand}')

class DisassembleState(AbstractState):
    """This state provides a disassembler."""

    def __init__(self: Self, state_machine: StateMachine) -> None:
        """
        Create an object of class `DisassembleState`.

        Parameters
        ----------
        state_machine : StateMachine
            The controlling `StateMachine` object.

        Postconditions
        --------------
        >>> self.current_opcode is None
        >>> self.current_operand is None
        >>> self.current_operand_size == 0
        >>> self.flags == 0x00
        >>> not self.until_return
        """
        super().__init__(state_machine)
        self.current_opcode: bytes | None = None
        self.current_operand: int | None = None
        self.current_operand_size = 0
        self.flags = 0x00
        self.until_return = False

        # Initialize this own instruction table.
        instructions = list(DEFAULT_INSTRUCTIONS)
        overrides = self._init_instructions()
        for opcode, instruction in overrides.items():
            instructions[opcode] = instruction
        self.instructions = instructions

    def __call__(self: Self, context: ContextT) -> tuple[ContextT, str|None]:
        """Disassemble bytes.

        Parameters
        ----------
        context : dict
            Depends on your application.

        Returns
        -------
        context : dict
            Depends on your application.
        next_state : str
            The name of the next state for the state machine.
        """

        while not self._is_terminated():
            instruction, operand_raw, across_bb = self._read_instruction()
            context, next_state = self._eval_instruction(
                instruction, across_bb, context)
            self._print_instruction(
                instruction, operand_raw, across_bb)
            if next_state:
                return context, next_state

        return context, None

    def runtime_init(self: Self, **kwargs) -> None:
        """Initialize before running the state machine.

        Parameters
        ----------
        flags : int, optional, default: 0
            The initial value of the register status bits.
        until_return : bool, optional, default: False
            Immediately terminate processing when RTI, RTS, or RTL
            instruction is processed.

        Postconditions
        --------------
        >>> self.current_opcode is None
        >>> self.current_operand is None
        >>> self.current_operand_size == 0
        >>> self.flags == 0x00
        >>> not self.until_return

        See also
        --------
        `StateMachine.runtime_init`
        """

        self.current_opcode = None
        self.current_operand = None
        self.current_operand_size = 0
        self.flags = kwargs.get('flags', 0)
        self.until_return = kwargs.get('until_return', False)

    def _is_terminated(self: Self) -> bool:
        """Determine if this state machine is terminated.

        When --until-return option is enabled,
        detection of the first RTI/RTS/RTL instruction terminates
        the main loop.

        Returns
        -------
        is_terminated : bool
            True if this state machine is to be terminated.
        """

        assert self.state_machine

        fsm = self.state_machine
        assert fsm.rom

        if (self.until_return and
                self.current_opcode in (b'\x40', b'\x60', b'\x6B')):
            return True

        return fsm.last_rom_addr <= fsm.rom.tell()

    def _read_instruction(
            self: Self
            ) -> tuple[type[AbstractInstruction], bytes, bool]:
        """Read the current instruction and return as an object."""

        assert self.state_machine
        fsm = self.state_machine

        # Read the opcode.
        opcode = fsm.rom.read(1)
        self.current_opcode = opcode
        instruction = self.get_instruction(opcode)

        self.current_operand_size = instruction.actual_operand_size(self.flags)

        # Test if PC crossed the bank boundary after the current
        # instraction's opcode has been read.
        if fsm.program_counter & 0xFFFF == 0x0000 and self.current_operand_size:
            self.current_operand_size = 0
            return instruction, bytes(), True

        # Test if PC crossed the bank boundary after the opcode
        # has been read.
        across_bb = False
        cur_counter = 0xFFFF & fsm.program_counter
        num_remain_bytes = 0x10000 - cur_counter
        if num_remain_bytes < self.current_operand_size:
            across_bb = True
            self.current_operand_size = num_remain_bytes

        # Read the operand if necessary.
        if self.current_operand_size:
            operand_raw = fsm.rom.read(self.current_operand_size)
            self.current_operand = int.from_bytes(operand_raw, 'little')
        else:
            operand_raw, self.current_operand = bytes(), None

        return instruction, operand_raw, across_bb

    def _eval_instruction(
            self: Self,
            instruction: type[AbstractInstruction],
            across_bb: bool,
            context: ContextT
            ) -> tuple[ContextT, str | None]:
        """Execute the current instruction.

        Parameters
        ----------
        instruction : AbstractInstruction
            The instruction to be output to `self.destination`.
        operand_raw : bytes
            The unprocessed operand bytes in the ROM image.
        across_bb : bool
            True if this line goes across the PB boundary.

        Returns
        -------
        context : dict
            Depends on your application.
        next_state : str
            The name of the next state for the state machine.
        """

        if not across_bb:
            return instruction.execute(self, context)

        return context, None

    def _print_instruction(
            self: Self,
            instruction: type[AbstractInstruction],
            operand_raw: bytes|None,
            across_bb: bool
            ) -> None:
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

        assert self.state_machine
        fsm = self.state_machine

        # cpu_addr is the value of PC immediately before reading
        # the current opcode.
        addr = fsm.program_counter - self.current_operand_size - 1
        out = fsm.destination
        operand_str = operand_raw.hex().upper() if operand_raw else ''
        mnemonic = instruction.mnemonic if not across_bb else ''
        operand = instruction.format(self) if not across_bb else ''

        print(OUTPUT_FORMAT.format(
            bank=(addr & 0xFF0000) >> 16,
            addr=addr & 0x00FFFF,
            opcode=instruction.opcode,
            operand_raw=operand_str,
            mnemonic=mnemonic,
            operand=operand).strip(),
              file=out)

    def _init_instructions(self: Self) -> dict:
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

    def get_instruction(
            self: Self,
            opcode: bytes
            ) -> type[AbstractInstruction]:
        """Return an object of class `AbstractInstruction`.

        Parameters
        ----------
        opcode : bytes
            A 1 byte value.

        Returns
        -------
        instruction : AbstractInstruction
            An object for one of instruction of the 65816 Processor.

        Raises
        ------
        IndexError
            If `opcode` is less zero or greater than 0xFF.

        Preconditions
        -------------
        >>> isinstance(opcode, (bytes, int,))
        """

        if isinstance(opcode, bytes):
            return self.instructions[int.from_bytes(opcode, 'little')]
        else:
            return self.instructions[opcode]

FORMAT_STRING = '{:02X}/{:04X}:\t{}'

class DumpState(AbstractState):
    """This state provides `hexdump`."""

    def __init__(self: Self, state_machine: StateMachine) -> None:
        """
        Create an object of class `DumpState`.

        Parameters
        ----------
        state_machine : StateMachine
            The controlling `StateMachine` object.

        Postconditions
        --------------
        >>> self.byte_count == tuple()
        >>> self.record_count == 0
        """
        super().__init__(state_machine)
        self.byte_count: Sequence = ()
        self.record_count = 0

    def __call__(self: Self, context: ContextT) -> tuple[ContextT, str | None]:
        """
        Perform byte-by-byte dump the contents of a ROM, in hexadecimal format.

        Parameters
        ----------
        context : dict
            Depends on your application.

        Returns
        -------
        context : dict
            Depends on your application.
        next_state : str
            The name of the next state for the state machine.
        """

        assert self.state_machine

        # Expermentally implement Disasm-Dump-Disasm
        # state-transition.
        next_state = context.pop('next_state', None)
        if next_state:
            self.byte_count = context.pop('byte_count', self.byte_count)
            self.record_count = context.pop('record_count', self.record_count)

        if not any(self.byte_count) or not self.record_count:
            return context, None

        fsm = self.state_machine
        rom = fsm.rom
        out = fsm.destination
        byte_count_seq = chain.from_iterable(
            repeat(self.byte_count, self.record_count))
        for i in byte_count_seq:
            cpu_address = fsm.program_counter
            bank = (cpu_address & 0xFF0000) >> 16
            offset = cpu_address & 0x00FFFF

            if offset + i > 0x10000:
                data = rom.read(0x10000 - offset)
            else:
                data = rom.read(i)

            print(FORMAT_STRING.format(
                bank, offset, data.hex().upper()),
                  file=out)

            if len(data) < i:
                return context, next_state

        return context, next_state

    def runtime_init(self: Self, **kwargs) -> None:
        """Initialize before running the state machine.

        Parameters
        ----------
        byte_count : list, optional
            A list containts the numbers of bytes per a record.
        record_count : int, optional
            The number of records.

        See also
        --------
        `StateMachine.runtime_init`
        """

        self.byte_count = kwargs.get('byte_count', ())
        self.record_count = kwargs.get('record_count', 0)
