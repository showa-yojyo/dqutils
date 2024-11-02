"""
Instructions of the 65816 Processor.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from dqutils.snescpu.addressing import get_addressing_mode

if TYPE_CHECKING:
    from collections.abc import MutableMapping
    from typing import Any

    from dqutils.snescpu.states import DisassembleState

    type ContextT = MutableMapping[str, Any]


def _execute_c2(state: DisassembleState, context: ContextT) -> tuple[ContextT, None]:
    """REP: Reset status bits.

    When used, it will set the bits specified by the 1 byte immediate
    value. This is the only means of setting the M and X status
    register bits.
    """
    assert isinstance(state.current_operand, int)
    state.flags &= ~state.current_operand
    return context, None


def _execute_e2(state: DisassembleState, context: ContextT) -> tuple[ContextT, None]:
    """SEP: Set status bits.

    When used, it will set the bits specified by the 1 byte immediate
    value. This is the only means of setting the M and X status
    register bits.
    """
    assert isinstance(state.current_operand, int)
    state.flags |= state.current_operand
    return context, None


# 65816 Programming Primer, Appendix B Composite Instruction List
# fmt: off
INSTRUCTION_TABLE = (
    ('BRK', 'Stack/Interrupt                ', 2, '**',),  # 00
    ('ORA', 'DP Indexed Indirect,X          ', 2, None,),  # 01
    ('COP', 'Stack/Interrupt                ', 2, '**',),  # 02
    ('ORA', 'Stack Relative                 ', 2, None,),  # 03
    ('TSB', 'Direct Page                    ', 2, None,),  # 04
    ('ORA', 'Direct Page                    ', 2, None,),  # 05
    ('ASL', 'Direct Page                    ', 2, None,),  # 06
    ('ORA', 'Direct Page Indirect Long      ', 2, None,),  # 07
    ('PHP', 'Stack (Push)                   ', 1, None,),  # 08
    ('ORA', 'Immediate                      ', 2, '*', ),  # 09
    ('ASL', 'Accumulator                    ', 1, None,),  # 0A
    ('PHD', 'Stack (Push)                   ', 1, None,),  # 0B
    ('TSB', 'Absolute                       ', 3, None,),  # 0C
    ('ORA', 'Absolute                       ', 3, None,),  # 0D
    ('ASL', 'Absolute                       ', 3, None,),  # 0E
    ('ORA', 'Absolute Long                  ', 4, None,),  # 0F
    ('BPL', 'Program Counter Relative       ', 2, None,),  # 10
    ('ORA', 'DP Indirect Indexed,Y          ', 2, None,),  # 11
    ('ORA', 'Direct Page Indirect           ', 2, None,),  # 12
    ('ORA', 'SR Indirect Indexed,Y          ', 2, None,),  # 13
    ('TRB', 'Direct Page                    ', 2, None,),  # 14
    ('ORA', 'Direct Page Indexed,X          ', 2, None,),  # 15
    ('ASL', 'Direct Page Indexed,X          ', 2, None,),  # 16
    ('ORA', 'DP Indirect Long Indexed,Y     ', 2, None,),  # 17
    ('CLC', 'Implied                        ', 1, None,),  # 18
    ('ORA', 'Absolute Indexed,Y             ', 3, None,),  # 19
    ('INC', 'Accumulator                    ', 1, None,),  # 1A
    ('TCS', 'Implied                        ', 1, None,),  # 1B
    ('TRB', 'Absolute                       ', 3, None,),  # 1C
    ('ORA', 'Absolute Indexed,X             ', 3, None,),  # 1D
    ('ASL', 'Absolute Indexed,X             ', 3, None,),  # 1E
    ('ORA', 'Absolute Long Indexed,X        ', 4, None,),  # 1F
    ('JSR', 'Absolute                       ', 3, None,),  # 20
    ('AND', 'DP Indexed Indirect,X          ', 2, None,),  # 21
    ('JSR', 'Absolute Long                  ', 4, None,),  # 22
    ('AND', 'Stack Relative                 ', 2, None,),  # 23
    ('BIT', 'Direct Page                    ', 2, None,),  # 24
    ('AND', 'Direct Page                    ', 2, None,),  # 25
    ('ROL', 'Direct Page                    ', 2, None,),  # 26
    ('AND', 'Direct Page Indirect Long      ', 2, None,),  # 27
    ('PLP', 'Stack (Pull)                   ', 1, None,),  # 28
    ('AND', 'Immediate                      ', 2, '*', ),  # 29
    ('ROL', 'Accumulator                    ', 1, None,),  # 2A
    ('PLD', 'Stack (Pull)                   ', 1, None,),  # 2B
    ('BIT', 'Absolute                       ', 3, None,),  # 2C
    ('AND', 'Absolute                       ', 3, None,),  # 2D
    ('ROL', 'Absolute                       ', 3, None,),  # 2E
    ('AND', 'Absolute Long                  ', 4, None,),  # 2F
    ('BMI', 'Program Counter Relative       ', 2, None,),  # 30
    ('AND', 'DP Indirect Indexed,Y          ', 2, None,),  # 31
    ('AND', 'Direct Page Indirect           ', 2, None,),  # 32
    ('AND', 'SR Indirect Indexed,Y          ', 2, None,),  # 33
    ('BIT', 'Direct Page Indexed,X          ', 2, None,),  # 34
    ('AND', 'Direct Page Indexed,X          ', 2, None,),  # 35
    ('ROL', 'Direct Page Indexed,X          ', 2, None,),  # 36
    ('AND', 'DP Indirect Long Indexed,Y     ', 2, None,),  # 37
    ('SEC', 'Implied                        ', 1, None,),  # 38
    ('AND', 'Absolute Indexed,Y             ', 3, None,),  # 39
    ('DEC', 'Accumulator                    ', 1, None,),  # 3A
    ('TSC', 'Implied                        ', 1, None,),  # 3B
    ('BIT', 'Absolute Indexed,X             ', 3, None,),  # 3C
    ('AND', 'Absolute Indexed,X             ', 3, None,),  # 3D
    ('ROL', 'Absolute Indexed,X             ', 3, None,),  # 3E
    ('AND', 'Absolute Long Indexed,X        ', 4, None,),  # 3F
    ('RTI', 'Stack/RTI                      ', 1, None,),  # 40
    ('EOR', 'DP Indexed Indirect,X          ', 2, None,),  # 41
    ('WDM', '                               ', 2, None,),  # 42
    ('EOR', 'Stack Relative                 ', 2, None,),  # 43
    ('MVP', 'Block Move                     ', 3, None,),  # 44
    ('EOR', 'Direct Page                    ', 2, None,),  # 45
    ('LSR', 'Direct Page                    ', 2, None,),  # 46
    ('EOR', 'Direct Page Indirect Long      ', 2, None,),  # 47
    ('PHA', 'Stack (Push)                   ', 1, None,),  # 48
    ('EOR', 'Immediate                      ', 2, '*', ),  # 49
    ('LSR', 'Accumulator                    ', 1, None,),  # 4A
    ('PHK', 'Stack (Push)                   ', 1, None,),  # 4B
    ('JMP', 'Absolute                       ', 3, None,),  # 4C
    ('EOR', 'Absolute                       ', 3, None,),  # 4D
    ('LSR', 'Absolute                       ', 3, None,),  # 4E
    ('EOR', 'Absolute Long                  ', 4, None,),  # 4F
    ('BVC', 'Program Counter Relative       ', 2, None,),  # 50
    ('EOR', 'DP Indirect Indexed,Y          ', 2, None,),  # 51
    ('EOR', 'Direct Page Indirect           ', 2, None,),  # 52
    ('EOR', 'SR Indirect Indexed,Y          ', 2, None,),  # 53
    ('MVN', 'Block Move                     ', 3, None,),  # 54
    ('EOR', 'Direct Page Indexed,X          ', 2, None,),  # 55
    ('LSR', 'Direct Page Indexed,X          ', 2, None,),  # 56
    ('EOR', 'DP Indirect Long Indexed,Y     ', 2, None,),  # 57
    ('CLI', 'Implied                        ', 1, None,),  # 58
    ('EOR', 'Absolute Indexed,Y             ', 3, None,),  # 59
    ('PHY', 'Stack (Push)                   ', 1, None,),  # 5A
    ('TCD', 'Implied                        ', 1, None,),  # 5B
    ('JMP', 'Absolute Long                  ', 4, None,),  # 5C
    ('EOR', 'Absolute Indexed,X             ', 3, None,),  # 5D
    ('LSR', 'Absolute Indexed,X             ', 3, None,),  # 5E
    ('EOR', 'Absolute Long Indexed,X        ', 4, None,),  # 5F
    ('RTS', 'Stack (RTS)                    ', 1, None,),  # 60
    ('ADC', 'DP Indexed Indirect,X          ', 2, None,),  # 61
    ('PER', 'Stack (PC Relative Long)       ', 3, None,),  # 62
    ('ADC', 'Stack Relative                 ', 2, None,),  # 63
    ('STZ', 'Direct Page                    ', 2, None,),  # 64
    ('ADC', 'Direct Page                    ', 2, None,),  # 65
    ('ROR', 'Direct Page                    ', 2, None,),  # 66
    ('ADC', 'Direct Page Indirect Long      ', 2, None,),  # 67
    ('PLA', 'Stack (Pull)                   ', 1, None,),  # 68
    ('ADC', 'Immediate                      ', 2, '*', ),  # 69
    ('ROR', 'Accumulator                    ', 1, None,),  # 6A
    ('RTL', 'Stack (RTL)                    ', 1, None,),  # 6B
    ('JMP', 'Absolute Indirect              ', 3, None,),  # 6C
    ('ADC', 'Absolute                       ', 3, None,),  # 6D
    ('ROR', 'Absolute                       ', 3, None,),  # 6E
    ('ADC', 'Absolute Long                  ', 4, None,),  # 6F
    ('BVS', 'Program Counter Relative       ', 2, None,),  # 70
    ('ADC', 'DP Indirect Indexed,Y          ', 2, None,),  # 71
    ('ADC', 'Direct Page Indirect           ', 2, None,),  # 72
    ('ADC', 'SR Indirect Indexed,Y          ', 2, None,),  # 73
    ('STZ', 'Direct Page Indexed,X          ', 2, None,),  # 74
    ('ADC', 'Direct Page Indexed,X          ', 2, None,),  # 75
    ('ROR', 'Direct Page Indexed,X          ', 2, None,),  # 76
    ('ADC', 'DP Indirect Long Indexed,Y     ', 2, None,),  # 77
    ('SEI', 'Implied                        ', 1, None,),  # 78
    ('ADC', 'Absolute Indexed,Y             ', 3, None,),  # 79
    ('PLY', 'Stack (Pull)                   ', 1, None,),  # 7A
    ('TDC', 'Implied                        ', 1, None,),  # 7B
    ('JMP', 'Absolute Indexed Indirect      ', 3, None,),  # 7C
    ('ADC', 'Absolute Indexed,X             ', 3, None,),  # 7D
    ('ROR', 'Absolute Indexed,X             ', 3, None,),  # 7E
    ('ADC', 'Absolute Long Indexed,X        ', 4, None,),  # 7F
    ('BRA', 'Program Counter Relative       ', 2, None,),  # 80
    ('STA', 'DP Indexed Indirect,X          ', 2, None,),  # 81
    ('BRL', 'Program Counter Relative Long  ', 3, None,),  # 82
    ('STA', 'Stack Relative                 ', 2, None,),  # 83
    ('STY', 'Direct Page                    ', 2, None,),  # 84
    ('STA', 'Direct Page                    ', 2, None,),  # 85
    ('STX', 'Direct Page                    ', 2, None,),  # 86
    ('STA', 'Direct Page Indirect Long      ', 2, None,),  # 87
    ('DEY', 'Implied                        ', 1, None,),  # 88
    ('BIT', 'Immediate                      ', 2, '*', ),  # 89
    ('TXA', 'Implied                        ', 1, None,),  # 8A
    ('PHB', 'Stack (Push)                   ', 1, None,),  # 8B
    ('STY', 'Absolute                       ', 3, None,),  # 8C
    ('STA', 'Absolute                       ', 3, None,),  # 8D
    ('STX', 'Absolute                       ', 3, None,),  # 8E
    ('STA', 'Absolute Long                  ', 4, None,),  # 8F
    ('BCC', 'Program Counter Relative       ', 2, None,),  # 90
    ('STA', 'DP Indirect Indexed,Y          ', 2, None,),  # 91
    ('STA', 'Direct Page Indirect           ', 2, None,),  # 92
    ('STA', 'SR Indirect Indexed,Y          ', 2, None,),  # 93
    ('STY', 'Direct Page Indexed,X          ', 2, None,),  # 94
    ('STA', 'Direct Page Indexed,X          ', 2, None,),  # 95
    ('STX', 'Direct Page Indexed,Y          ', 2, None,),  # 96
    ('STA', 'DP Indirect Long Indexed,Y     ', 2, None,),  # 97
    ('TYA', 'Implied                        ', 1, None,),  # 98
    ('STA', 'Absolute Indexed,Y             ', 3, None,),  # 99
    ('TXS', 'Implied                        ', 1, None,),  # 9A
    ('TXY', 'Implied                        ', 1, None,),  # 9B
    ('STZ', 'Absolute                       ', 3, None,),  # 9C
    ('STA', 'Absolute Indexed,X             ', 3, None,),  # 9D
    ('STZ', 'Absolute Indexed,X             ', 3, None,),  # 9E
    ('STA', 'Absolute Long Indexed,X        ', 4, None,),  # 9F
    ('LDY', 'Immediate                      ', 2, '+', ),  # A0
    ('LDA', 'DP Indexed Indirect,X          ', 2, None,),  # A1
    ('LDX', 'Immediate                      ', 2, '+', ),  # A2
    ('LDA', 'Stack Relative                 ', 2, None,),  # A3
    ('LDY', 'Direct Page                    ', 2, None,),  # A4
    ('LDA', 'Direct Page                    ', 2, None,),  # A5
    ('LDX', 'Direct Page                    ', 2, None,),  # A6
    ('LDA', 'Direct Page Indirect Long      ', 2, None,),  # A7
    ('TAY', 'Implied                        ', 1, None,),  # A8
    ('LDA', 'Immediate                      ', 2, '*', ),  # A9
    ('TAX', 'Implied                        ', 1, None,),  # AA
    ('PLB', 'Stack (Pull)                   ', 1, None,),  # AB
    ('LDY', 'Absolute                       ', 3, None,),  # AC
    ('LDA', 'Absolute                       ', 3, None,),  # AD
    ('LDX', 'Absolute                       ', 3, None,),  # AE
    ('LDA', 'Absolute Long                  ', 4, None,),  # AF
    ('BCS', 'Program Counter Relative       ', 2, None,),  # B0
    ('LDA', 'DP Indirect Indexed,Y          ', 2, None,),  # B1
    ('LDA', 'Direct Page Indirect           ', 2, None,),  # B2
    ('LDA', 'SR Indirect Indexed,Y          ', 2, None,),  # B3
    ('LDY', 'Direct Page Indexed,X          ', 2, None,),  # B4
    ('LDA', 'Direct Page Indexed,X          ', 2, None,),  # B5
    ('LDX', 'Direct Page Indexed,Y          ', 2, None,),  # B6
    ('LDA', 'DP Indirect Long Indexed,Y     ', 2, None,),  # B7
    ('CLV', 'Implied                        ', 1, None,),  # B8
    ('LDA', 'Absolute Indexed,Y             ', 3, None,),  # B9
    ('TSX', 'Implied                        ', 1, None,),  # BA
    ('TYX', 'Implied                        ', 1, None,),  # BB
    ('LDY', 'Absolute Indexed,X             ', 3, None,),  # BC
    ('LDA', 'Absolute Indexed,X             ', 3, None,),  # BD
    ('LDX', 'Absolute Indexed,Y             ', 3, None,),  # BE
    ('LDA', 'Absolute Long Indexed,X        ', 4, None,),  # BF
    ('CPY', 'Immediate                      ', 2, '+', ),  # C0
    ('CMP', 'DP Indexed Indirect,X          ', 2, None,),  # C1
    ('REP', 'Immediate                      ', 2, None,),  # C2
    ('CMP', 'Stack Relative                 ', 2, None,),  # C3
    ('CPY', 'Direct Page                    ', 2, None,),  # C4
    ('CMP', 'Direct Page                    ', 2, None,),  # C5
    ('DEC', 'Direct Page                    ', 2, None,),  # C6
    ('CMP', 'Direct Page Indirect Long      ', 2, None,),  # C7
    ('INY', 'Implied                        ', 1, None,),  # C8
    ('CMP', 'Immediate                      ', 2, '*', ),  # C9
    ('DEX', 'Implied                        ', 1, None,),  # CA
    ('WAI', 'Implied                        ', 1, None,),  # CB
    ('CPY', 'Absolute                       ', 3, None,),  # CC
    ('CMP', 'Absolute                       ', 3, None,),  # CD
    ('DEC', 'Absolute                       ', 3, None,),  # CE
    ('CMP', 'Absolute Long                  ', 4, None,),  # CF
    ('BNE', 'Program Counter Relative       ', 2, None,),  # D0
    ('CMP', 'DP Indirect Indexed,Y          ', 2, None,),  # D1
    ('CMP', 'Direct Page Indirect           ', 2, None,),  # D2
    ('CMP', 'SR Indirect Indexed,Y          ', 2, None,),  # D3
    ('PEI', 'Stack (Direct Page Indirect)   ', 2, None,),  # D4
    ('CMP', 'Direct Page Indexed,X          ', 2, None,),  # D5
    ('DEC', 'Direct Page Indexed,X          ', 2, None,),  # D6
    ('CMP', 'DP Indirect Long Indexed,Y     ', 2, None,),  # D7
    ('CLD', 'Implied                        ', 1, None,),  # D8
    ('CMP', 'Absolute Indexed,Y             ', 3, None,),  # D9
    ('PHX', 'Stack (Push)                   ', 1, None,),  # DA
    ('STP', 'Implied                        ', 1, None,),  # DB
    ('JMP', 'Absolute Indirect Long         ', 3, None,),  # DC
    ('CMP', 'Absolute Indexed,X             ', 3, None,),  # DD
    ('DEC', 'Absolute Indexed,X             ', 3, None,),  # DE
    ('CMP', 'Absolute Long Indexed,X        ', 4, None,),  # DF
    ('CPX', 'Immediate                      ', 2, '+', ),  # E0
    ('SBC', 'DP Indexed Indirect,X          ', 2, None,),  # E1
    ('SEP', 'Immediate                      ', 2, None,),  # E2
    ('SBC', 'Stack Relative                 ', 2, None,),  # E3
    ('CPX', 'Direct Page                    ', 2, None,),  # E4
    ('SBC', 'Direct Page                    ', 2, None,),  # E5
    ('INC', 'Direct Page                    ', 2, None,),  # E6
    ('SBC', 'Direct Page Indirect Long      ', 2, None,),  # E7
    ('INX', 'Implied                        ', 1, None,),  # E8
    ('SBC', 'Immediate                      ', 2, '*', ),  # E9
    ('NOP', 'Implied                        ', 1, None,),  # EA
    ('XBA', 'Implied                        ', 1, None,),  # EB
    ('CPX', 'Absolute                       ', 3, None,),  # EC
    ('SBC', 'Absolute                       ', 3, None,),  # ED
    ('INC', 'Absolute                       ', 3, None,),  # EE
    ('SBC', 'Absolute Long                  ', 4, None,),  # EF
    ('BEQ', 'Program Counter Relative       ', 2, None,),  # F0
    ('SBC', 'DP Indirect Indexed,Y          ', 2, None,),  # F1
    ('SBC', 'Direct Page Indirect           ', 2, None,),  # F2
    ('SBC', 'SR Indirect Indexed,Y          ', 2, None,),  # F3
    ('PEA', 'Stack (Absolute)               ', 3, None,),  # F4
    ('SBC', 'Direct Page Indexed,X          ', 2, None,),  # F5
    ('INC', 'Direct Page Indexed,X          ', 2, None,),  # F6
    ('SBC', 'DP Indirect Long Indexed,Y     ', 2, None,),  # F7
    ('SED', 'Implied                        ', 1, None,),  # F8
    ('SBC', 'Absolute Indexed,Y             ', 3, None,),  # F9
    ('PLX', 'Stack (Pull)                   ', 1, None,),  # FA
    ('XCE', 'Implied                        ', 1, None,),  # FB
    ('JSR', 'Absolute Indexed Indirect      ', 3, None,),  # FC
    ('SBC', 'Absolute Indexed,X             ', 3, None,),  # FD
    ('INC', 'Absolute Indexed,X             ', 3, None,),  # FE
    ('SBC', 'Absolute Long Indexed,X        ', 4, None,),) # FF
# *  Add 1 if m=0 (16 bit memory/accumulator).
# +  Add 1 byte if x=0 (16-bit index registers).
# ** Opcode is 1 byte, but program counter value pushed onto stack is
#    incremented by 2 allowing for optional signature byte.
# fmt: on


class AbstractInstruction:
    """The base class for all instruction classes."""

    opcode = None
    operand_size: int
    mnemonic = None
    # aliases = None
    add_if_m_zero: bool
    add_if_x_zero: bool
    addressing_mode = None

    @classmethod
    def actual_operand_size(cls, flags: int) -> int:
        """Return the actual size of this operand in bytes."""

        # Addition for Immediate mode.
        if cls.add_if_x_zero and flags & 0x10 == 0x00 or cls.add_if_m_zero and flags & 0x20 == 0x00:
            return cls.operand_size

        return cls.operand_size - 1

    @staticmethod
    def execute(state: DisassembleState, context: ContextT) -> tuple[ContextT, str | None]:
        """Overrided by subclasses if necessary.

        Parameters
        ----------
        state : DisassembleState
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

    @classmethod
    def format(cls, state: DisassembleState) -> str:
        """Return formatted string of this instruction.

        Parameters
        ----------
        cls : AbstractInstruction
        state : DisassembleState

        Returns
        -------
        result : str
            A string value which contains its name and parsed
            operand.
        """

        if not (addressing_mode := cls.addressing_mode):
            # Opcode 42, WDM.
            assert state.current_operand
            return f"#${state.current_operand:02X}"

        if addressing_mode.formatter:
            return addressing_mode.formatter(state)

        if syntax := addressing_mode.syntax:
            return syntax.format(state.current_operand)

        return ""


def _build_instruction_classes() -> list[type[AbstractInstruction]]:
    """Register newly generated types to this module."""

    global_dicts = globals()
    # inst_classes = {}
    instructions = []
    for opcode, cols in enumerate(INSTRUCTION_TABLE):
        attrs = {
            "__slots__": (),
            "opcode": opcode,
            "mnemonic": cols[0],
            "addressing_mode": get_addressing_mode(cols[1]),
            "operand_size": int(cols[2]),
        }

        annotation = cols[3]
        attrs["add_if_m_zero"] = annotation == "*"
        attrs["add_if_x_zero"] = annotation == "+"

        if method := global_dicts.get(f"_execute_{opcode:02x}"):
            attrs["execute"] = method

        cls = type(f"Instruction{opcode:02X}", (AbstractInstruction,), attrs)
        # inst_classes[class_name] = cls
        instructions.append(cls)

    # global_dicts.update(inst_classes)
    return instructions


def get_instruction(opcode: bytes | int) -> type[AbstractInstruction]:
    """Return the instruction object by its opcode.

    Parameters
    ----------
    opcode : bytes
        A one byte value. See also `INSTRUCTION_TABLE`.

    Returns
    -------
    instruction : AbstractInstruction
        An object for one of instruction of the 65816 Processor.

    Raises
    ------
    IndexError
        If `opcode` is invalid opcode for the 65816 Processor.
    """

    if isinstance(opcode, bytes):
        opcode = int.from_bytes(opcode, "little")

    assert isinstance(opcode, int)
    return DEFAULT_INSTRUCTIONS[opcode]


DEFAULT_INSTRUCTIONS = tuple(_build_instruction_classes())
