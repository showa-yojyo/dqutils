"""
Provide a state machine for the 65816 Processor.
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from .mapper import make_mapper

if TYPE_CHECKING:
    from collections.abc import Iterable
    import mmap
    from typing import Self
    from .mapper import AbstractMapper
    from .states import AbstractState, ContextT


class StateMachine(object):
    """A state machine for the 65816 CPU disassembler."""

    def __init__(
        self: Self,
        state_classes: Iterable[type[AbstractState]],
        initial_state: str,
        rom: mmap.mmap,
        mapper: type[AbstractMapper] | None = None,
    ) -> None:
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

        Postconditions
        --------------
        >>> self.rom is rom
        >>> self.initial_state == initial_state
        >>> self.current_state == initial_state
        >>> self.destination is sys.stdout
        """

        self.rom = rom
        self.mapper = mapper if mapper else make_mapper(rom=rom)
        self.last_rom_addr: int

        self.initial_state = initial_state
        self.current_state = initial_state
        self.states: dict[str, AbstractState] = {}
        self.add_states(state_classes)

        self.destination = sys.stdout

    @property
    def program_counter(self: Self) -> int:
        """Return the program counter.

        Returns
        -------
        pc : int
        """
        assert self.rom and self.mapper
        return self.mapper.from_rom(self.rom.tell())

    def unlink(self: Self) -> None:
        """Remove circular references.

        Postconditions
        --------------
        >>> self.states == {}
        """

        for i in self.states.values():
            i.unlink()
        self.states = {}

    def add_states(self: Self, state_classes: Iterable[type[AbstractState]]) -> None:
        """Add state classes to `self.states`.

        Parameters
        ----------
        state_classes : list
            A list of `State` subclasses.
        """

        self.states.update({state_t.__name__: state_t(self) for state_t in state_classes})

    def runtime_init(self: Self, **kwargs) -> None:
        """Initialize states before running the state machine.

        Preconditions
        -------------
        >>> isinstance(self.states, dict)
        """
        for i in self.states.values():
            i.runtime_init(**kwargs)

    def run(self: Self, **kwargs) -> None:
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

        self.current_state = kwargs.get("initial_state", self.initial_state)

        first = kwargs.get("first", 0)
        last = kwargs.get("last", -1)

        self.rom.seek(self.mapper.from_cpu(first))
        self.last_rom_addr = self.mapper.from_cpu(last) if last != -1 else self.rom.size()
        self.runtime_init(**kwargs)

        state = self.get_state()
        context: ContextT = {}
        while state:
            context, next_state = state(context)
            if not next_state:
                break
            state = self.get_state(next_state)

    def get_state(self: Self, next_state: str | None = None) -> AbstractState:
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

        Preconditions
        -------------
        >>> isinstance(self.states, dict)

        Raises
        ------
        KeyError
            If `next_state` is not in `self.states`.
        """

        if next_state:
            self.current_state = next_state
        return self.states[self.current_state]
