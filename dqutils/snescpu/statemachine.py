"""
Provide a state machine for the 65816 Processor.
"""

import sys
from .mapper import make_mapper

class StateMachine(object):
    """A state machine for the 65816 CPU disassembler."""

    def __init__(self, state_classes, initial_state, rom, mapper=None):
        """Initialize an object of class `StateMachine`.

        Parameters
        ----------
        state_classes : list
            A list of `State` subclasses.
        initial_state : str
            The class name of the initial state.
        rom : mmap.mmap
            A ROM image object.
        mapper : AbstractMapper, optional
            The mapper to `rom`.
        """

        self.rom = rom
        if mapper:
            self.mapper = mapper
        else:
            self.mapper = make_mapper(rom=rom)

        self.last_rom_addr = 'dummy'

        self.initial_state = initial_state
        self.current_state = initial_state
        self.states = {} # {state_name: State}
        self.add_states(state_classes)

        self.destination = sys.stdout

    @property
    def program_counter(self):
        """Return the program counter.

        Returns
        -------
        pc : int
        """
        assert self.rom and self.mapper
        return self.mapper.from_rom(self.rom.tell())

    def unlink(self):
        """Remove circular references."""

        for i in self.states.values():
            i.unlink()
        self.states = None

    def add_states(self, state_classes):
        """Add state classes to `self.states`.

        Parameters:
        state_classes : list
            A list of `State` subclasses.
        """

        self.states.update(
            {state_t.__name__: state_t(self) for state_t in state_classes})

    def runtime_init(self, **kwargs):
        """Initialize states before running the state machine."""
        for i in self.states.values():
            i.runtime_init(**kwargs)

    def run(self, **kwargs):
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
        until_return : bool, optional, default: False
            Immediately terminate processing when RTI, RTS, or RTL
            instruction is processed.
        initial_state : State, optional, default: None
            The name of initial state.
        """

        self.current_state = kwargs.get('initial_state',
                                        self.initial_state)

        first = kwargs.get('first', 0)
        last = kwargs.get('last', -1)

        self.rom.seek(self.mapper.from_cpu(first))
        if last != -1:
            self.last_rom_addr = self.mapper.from_cpu(last)
        else:
            self.last_rom_addr = self.rom.size()

        self.runtime_init(**kwargs)

        state = self.get_state()
        while state:
            next_state = state()
            if not next_state:
                break
            state = self.get_state(next_state)

    def get_state(self, next_state=None):
        """Return the current state object.

        If `next_state` is specified, then it is set to
        `self.current_state`.

        Parameters
        ----------
        next_state : str
            The name of the next state.

        Returns
        -------
        current_state : State

        Raises
        ------
        KeyError is raised if `next_state` is not in `self.states`.
        """

        if next_state:
            self.current_state = next_state
        return self.states[self.current_state]
