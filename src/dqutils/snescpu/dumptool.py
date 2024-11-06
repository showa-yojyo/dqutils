"""
Example:
$ dumptool.py dqutils.dq3.dumptool 0xC8F323 0x36 10
#$0000\t#$00001F
#$0000\t#$0003E0
...
#$0035\t#$000001
[EOF]
"""

from __future__ import annotations

import sys
from argparse import ArgumentParser
from csv import QUOTE_NONE, reader, writer
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from _csv import _writer
    from argparse import Namespace
    from collections.abc import Iterable, Sequence
    from typing import Final, Literal

from dqutils.bit import get_bits
from dqutils.release import __version__
from dqutils.snescpu.mapper import make_mapper
from dqutils.snescpu.rom_image import RomImage


def int_wrapper(string: str) -> int:
    """A helper function."""

    if string.startswith("#$"):
        return int(string[2:], base=16)

    if string.startswith("$"):
        return int(string[1:], base=16)

    return int(string, 0)


def formatter(mask_bits: int) -> str:
    """A helper function."""

    numbits = bin(mask_bits).count("1")
    if numbits > 16:  # noqa: PLR2004
        return "{:06X}"
    if numbits > 8:  # noqa: PLR2004
        return "{:04X}"
    if numbits < 4:  # noqa: PLR2004
        return "{:d}"

    return "{:02X}"


COLUMN_OFFSET: Final[int] = 0
COLUMN_MASK_BITS: Final[int] = 1


def dump(
    title: str, address: int, sizeof_object: int, sizeof_array: int, source: Iterable, destination: _writer
) -> None:
    """Dump a sequence of typed objects in ROM image.

    Parameters
    ----------
    title: str
        The title of a game, e.g. 'DRAGONQUEST3'.
    address: int
        The address of the array in ROM space.
    sizeof_object: int
        length of the array, i.e. the number of objects.
    sizeof_array: int
        The size of the structure, class or object.
    source:
        A CSV reader object.
    destination:
        A CSV writer object.
    """

    members = [
        (
            int_wrapper(row[COLUMN_OFFSET]),
            int_wrapper(row[COLUMN_MASK_BITS]),
        )
        for row in source
    ]

    fmts = [formatter(i[COLUMN_MASK_BITS]) for i in members]

    with RomImage(title) as rom:
        mapper = make_mapper(rom)
        rom.seek(mapper.from_cpu(address))
        for i in range(sizeof_array):
            chunk = rom.read(sizeof_object)

            output = [f"{i:04X}"]
            output.extend(
                formatter.format(get_bits(chunk, member[COLUMN_OFFSET], member[COLUMN_MASK_BITS]))
                for (member, formatter) in zip(members, fmts, strict=False)
            )

            destination.writerow(output)


def parse_args(args: Sequence[str]) -> Namespace:
    parser = ArgumentParser(description="A dump tool")
    parser.add_argument(
        "address",
        type=int_wrapper,
        help="address of the array in ROM space",
    )
    parser.add_argument(
        "sizeof_object",
        type=int_wrapper,
        help="size of the structure, class or object",
    )
    parser.add_argument(
        "sizeof_array",
        type=int_wrapper,
        help="length of the array (or the number of objects)",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=__version__,
    )
    parser.add_argument(
        "--delimiter",
        default="\t",
        metavar="SEP",
        help="use SEP as fields separator (default to \\t)",
    )
    return parser.parse_args(args)


def run(title: str, args: Sequence[str] = sys.argv[1:]) -> Literal[0]:
    arguments = parse_args(args=args or ("--help",))
    delimiter = arguments.delimiter
    dump(
        title,
        arguments.address,
        arguments.sizeof_object,
        arguments.sizeof_array,
        reader(sys.stdin, delimiter=delimiter, quoting=QUOTE_NONE),
        writer(sys.stdout, delimiter=delimiter, quoting=QUOTE_NONE, lineterminator="\n"),
    )
    return 0
