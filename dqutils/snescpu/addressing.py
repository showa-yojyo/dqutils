"""
This module offers the addressing modes of the 65816 Processor.
"""

# Block Move

@staticmethod
def _format_block_move(fsm):
    """Block Move"""

    operand = fsm.current_operand
    return '${src:02X},${dest:02X}'.format(
        src=operand & 0x00FF,
        dest=(operand & 0xFF00) >> 8)

# Immediate

@staticmethod
def _format_immediate(fsm):
    """Immediate"""

    actual_operand_size = fsm.current_operand_size

    return '#${:0{width}X}'.format(
        fsm.current_operand, width=actual_operand_size * 2)

# Program Counter Relative

@staticmethod
def _format_program_counter_relative(fsm):
    """Program Counter Relative"""

    program_counter = fsm.program_counter
    operand = fsm.current_operand

    if operand & 0x80 == 0x00:
        near_addr = (program_counter + operand) & 0xFFFF
    else:
        near_addr = (program_counter - (0x100 - operand)) & 0xFFFF
    return '${:04X}'.format(near_addr)

@staticmethod
def _format_program_counter_relative_long(fsm):
    """Program Counter Relative Long"""

    program_counter = fsm.program_counter
    operand = fsm.current_operand
    if operand & 0x8000 == 0x0000:
        addr = (program_counter + operand) & 0xFFFF
    else:
        addr = (program_counter - (0x10000 - operand)) & 0xFFFF

    return '${:04X}'.format(addr)

# Stack

@staticmethod
def _format_stack_interrupt(fsm):
    """Stack/Interrupt"""

    # TODO: treat as if BRK/COP takes 2 bytes as operand.
    return '#${:02X}'.format(fsm.current_operand)

@staticmethod
def _format_stack_program_counter_relative_long(fsm):
    """Stack (PCounter Relative Long)"""
    return '${:04X}'.format(
        (fsm.program_counter + fsm.current_operand) & 0xFFFF)

# pylint: disable=line-too-long
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
    ('Stack/Interrupt              ', '#${:02X}       ', _format_stack_interrupt,),
    ('Stack/RTI                    ', '               ', None,),
)

def _build_addressing_mode_classes():
    """Register newly generated types to this module."""

    # pylint: disable=too-few-public-methods
    class AbstractAddressingMode(object):
        """The base class for all addressing mode classes."""

        name = None
        syntax = None
        formatter = None

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
            formatter=formatter,)

        addr_classes[class_name] = type(
            class_name, (AbstractAddressingMode,), attrs)

    global_dicts.update(addr_classes)

def get_addressing_mode(name):
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

    name_stripped = name.strip()
    if not name_stripped:
        # WDM
        return None

    return globals()[name_stripped]

_build_addressing_mode_classes()
