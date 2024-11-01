"""
This module offers the addressing modes of the 65816 Processor.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Callable
    from .states import DisassembleState

# Block Move


def _format_block_move(state: DisassembleState) -> str:
    """Block Move"""

    operand = state.current_operand or 0
    return f"${operand & 0x00FF:02X},${operand & 0xFF00 >> 8:02X}"


# Immediate


def _format_immediate(state: DisassembleState) -> str:
    """Immediate"""

    actual_operand_size = state.current_operand_size
    return f"#${state.current_operand:0{actual_operand_size * 2}X}"


# Program Counter Relative


def _format_program_counter_relative(state: DisassembleState) -> str:
    """Program Counter Relative"""

    program_counter = state.program_counter
    operand = state.current_operand or 0  # XXX

    if operand & 0x80 == 0x00:
        near_addr = (program_counter + operand) & 0xFFFF
    else:
        near_addr = (program_counter - (0x100 - operand)) & 0xFFFF
    return f"${near_addr:04X}"


def _format_program_counter_relative_long(state: DisassembleState) -> str:
    """Program Counter Relative Long"""

    program_counter = state.program_counter
    operand = state.current_operand or 0  # XXX
    if operand & 0x8000 == 0x0000:
        addr = (program_counter + operand) & 0xFFFF
    else:
        addr = (program_counter - (0x10000 - operand)) & 0xFFFF

    return f"${addr:04X}"


# Stack


def _format_stack_program_counter_relative_long(state: DisassembleState) -> str:
    """Stack (PCounter Relative Long)"""
    assert isinstance(state.current_operand, int)
    return f"${(state.program_counter + state.current_operand) & 0xFFFF:04X}"


# pylint: disable=line-too-long
# fmt: off
ADDRESSING_MODE_TABLE = (
    ('Absolute                     ', '${:04X}        ', None,),
    ('Absolute Indexed Indirect    ', '(${:04X},X)    ', None,),
    ('Absolute Indexed,X           ', '${:04X},X      ', None,),
    ('Absolute Indexed,Y           ', '${:04X},Y      ', None,),
    ('Absolute Indirect            ', '(${:04X})      ', None,),
    ('Absolute Indirect Long       ', '[${:04X}]      ', None,),
    ('Absolute Long                ', '${:06X}        ', None,),
    ('Absolute Long Indexed,X      ', '${:06X},X      ', None,),
    ('Accumulator                  ', 'A              ', None,),
    ('Block Move                   ', '${:02X},${:02X}', _format_block_move,),
    ('Direct Page                  ', '${:02X}        ', None,),
    ('Direct Page Indexed,X        ', '${:02X},X      ', None,),
    ('Direct Page Indexed,Y        ', '${:02X},Y      ', None,),
    ('Direct Page Indirect         ', '(${:02X})      ', None,),
    ('Direct Page Indirect Long    ', '[${:02X}]      ', None,),
    ('DP Indexed Indirect,X        ', '(${:02X},X)    ', None,),
    ('DP Indirect Indexed,Y        ', '(${:02X}),Y    ', None,),
    ('DP Indirect Long Indexed,Y   ', '[${:02X}],Y    ', None,),
    ('Immediate                    ', '#${:0{width}X} ', _format_immediate,),
    ('Implied                      ', '               ', None,),
    ('Program Counter Relative     ', '${:04X}        ', _format_program_counter_relative,),
    ('Program Counter Relative Long', '${:04X}        ', _format_program_counter_relative_long,),
    ('SR Indirect Indexed,Y        ', '(${:02X},S),Y  ', None,),
    ('Stack (Absolute)             ', '${:04X}        ', None,),
    ('Stack (Direct Page Indirect) ', '(${:02X})      ', None,),
    ('Stack (PC Relative Long)     ', '${:04X}        ', _format_stack_program_counter_relative_long,),
    ('Stack (Pull)                 ', '               ', None,),
    ('Stack (Push)                 ', '               ', None,),
    ('Stack (RTL)                  ', '               ', None,),
    ('Stack (RTS)                  ', '               ', None,),
    ('Stack Relative               ', '${:02X},S      ', None,),
    ('Stack/Interrupt              ', '#${:02X}       ', None,),
    ('Stack/RTI                    ', '               ', None,),
)
# fmt: on


# pylint: disable=too-few-public-methods
class AbstractAddressingMode(object):
    """The base class for all addressing mode classes."""

    name: str
    syntax: str
    formatter: Callable[[DisassembleState], str] | None


def _build_addressing_mode_classes() -> None:
    """Register newly generated types to this module."""

    global_dicts = globals()
    addr_classes = {}
    for cols in ADDRESSING_MODE_TABLE:
        class_name = cols[0].strip()
        syntax = cols[1].strip()
        formatter = cols[2]

        attrs = dict(
            __slots__=(),
            name=class_name,
            syntax=syntax,
            formatter=formatter,
        )

        addr_classes[class_name] = type(class_name, (AbstractAddressingMode,), attrs)

    global_dicts.update(addr_classes)


def get_addressing_mode(name: str) -> AbstractAddressingMode | None:
    """Return the addressing mode object by its name.

    If `name` is empty, ``None`` is returned.

    Parameters
    ----------
    name : str
        See also `ADDRESSING_MODE_TABLE`.

    Returns
    -------
    addr_mode : AbstractAddressingMode
        An object for one of addressing modes of the 65816 Processor.

    Raises
    ------
    KeyError
        If `name` is neither valid for addressing mode nor empty.
    """

    if name_stripped := name.strip():
        return globals()[name_stripped]

    # WDM
    return None


_build_addressing_mode_classes()
