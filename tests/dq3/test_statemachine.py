"""
Tests for dqutils.snescpu.statemachine.
"""

from io import StringIO

from snescpu.test_statemachine import AbstractStateMachineTestCase

from dqutils.dq3.disasm import DisassembleStateDQ3, DumpState


class StateMachineTestCase(AbstractStateMachineTestCase):
    """Tests for disassembling DQ3."""

    game_title = "DRAGONQUEST3"
    state_classes = (DisassembleStateDQ3, DumpState)
    initial_state = "DisassembleStateDQ3"

    def test_disassembled_code(self):
        """Test disassembled code for DQ3."""

        fsm = self.fsm
        fsm.destination = StringIO()
        fsm.run(first=0xC25BA6, last=0xC25BCE)

        output_lines = fsm.destination.getvalue().split("\n")
        self.assertRegex(output_lines[0], r"^C2/5BA6:\s+A20000\s+LDX #\$0000$")
        self.assertRegex(output_lines[-2], r"^C2/5BCD:\s+60\s+RTS$")
        self.assertEqual(output_lines[-1], "")

    def test_run_brk_operand(self):
        """Test if the operand of the BRK command is 2 bytes."""

        fsm = self.fsm
        fsm.destination = StringIO()

        # People in the Shrine of Dharma.
        fsm.run(first=0xCB9A3E, last=0xCB9A57)

        output_lines = fsm.destination.getvalue().split("\n")

        for i in (
            0,
            2,
            4,
            6,
        ):
            line = output_lines[i]
            self.assertRegex(line, r"^CB/[0-9A-F]{4}:\s+00[0-9A-F]{4}\s+")
            self.assertRegex(line, r"BRK #\$[0-9A-F]{4}$")

        self.assertRegex(output_lines[-2], r"^CB/9A56:\s+6B\s+RTL$")
        self.assertEqual(output_lines[-1], "")

    def test_run_cop_operand(self):
        """Test if the operand of the COP command varies."""

        fsm = self.fsm
        fsm.destination = StringIO()
        fsm.run(first=0xCC001B, until_return=True)
        actual = fsm.destination.getvalue().partition("\n")
        expected = "CC/001B:	02      	COP"
        self.assertEqual(expected, actual[0])

    def test_jsr_args(self):
        """Test outputs of JSR instructions that have arguments."""

        fsm = self.fsm
        fsm.destination = StringIO()

        # JSR $C90572 (RTL+B)
        fsm.run(first=0xC66C1B, until_return=True)
        actual = fsm.destination.getvalue()
        expected = (
            "C6/6C1B:	227205C9	JSR $C90572\n"
            "C6/6C1F:	00\n"
            "C6/6C20:	0700\n"
            "C6/6C22:	B17DC8\n"
            "C6/6C25:	0000\n"
            "C6/6C27:	1F0000\n"
            "C6/6C2A:	997DA1  	STA $A17D,Y\n"
            ""
        )
        self.assertIn(expected, actual)
