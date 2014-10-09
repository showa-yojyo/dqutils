# -*- coding: utf-8 -*-
"""dqutils.message module
"""

from dqutils.string import get_text
from dqutils.string import get_hex
from dqutils.rom_image import RomImage
from dqutils.string_generator import StringGeneratorCStyle
from array import array

def enum_battle(context, first=None, last=None):
    """Generate battle message data.

    Message data that indices in [`first`, `last`) will be output.

    Args:
      context: TBW
      first: The first index of the range you want.
      last: The last index + 1 of the range you want.

    Yields:
      A tuple of (address, shift-bits, character-code).
    """
    yield from StringGeneratorCStyle(context, first, last)

def print_battle(context, first=None, last=None):
    """Print message data to sys.stdout.

    Message data that indices in [`first`, `last`) will be output.

    Args:
      context: TBW
      first: The first index of the range you want.
      last: The last index + 1 of the range you want.

    Returns:
      None.
    """

    # Test preconditions.
    charmap = context["charmap"]
    assert charmap is None or isinstance(charmap, dict)

    delims = context["delimiters"]
    assert delims is None or isinstance(delims, bytes)

    for i, item in enumerate(enum_battle(context, first, last)):
        if charmap:
            text = get_text(item[1], charmap, delims)
        else:
            text = get_hex(item[1])

        print("{index:04X}:{address:06X}:{message}".format(
            index=i,
            address=item[0],
            message=text))

def enum_scenario(context, generator_t, first=None, last=None):
    """Generate scenario message data.

    Message data that indices in [`first`, `last`) will be output.

    Args:
      context: TBW
      generator_t: The type of message generator.
        See the module dqutils.message_generator for details.
      first: The first index of the range you want.
      last: The last index + 1 of the range you want.

    Yields:
      A tuple of (address, shift-bits, character-code).
    """

    # Test preconditions.
    assert "title" in context
    assert "message_id_first" in context or first is not None
    assert "message_id_last" in context or last is not None

    if not first:
        first = context["message_id_first"]
    if not last:
        last = context["message_id_last"]
    assert first < last

    with RomImage(context["title"]) as mem:
        # pylint: disable=star-args
        decoder = generator_t(**context)
        decoder.setup(mem)
        yield from decoder.enumerate(mem, first, last)

def print_scenario(context, generator_t, first=None, last=None):
    """Print message data to sys.stdout.

    Message data that indices in [`first`, `last`) will be output.

    Args:
      context: TBW
      generator_t: The type of message generator.
        See the module dqutils.message_generator for details.
      first: The first index of the range you want.
      last: The last index + 1 of the range you want.

    Returns:
      None.
    """

    charmap = context["charmap"]
    assert charmap is None or isinstance(charmap, dict)

    delims = context["delimiters"]
    assert delims is None or isinstance(delims, array)

    for i, item in enumerate(enum_scenario(context, generator_t, first, last)):
        address, shift, code_seq = item
        text = get_text(code_seq, charmap, delims)
        print("{index:04X}:{address:06X}:{shift:02X}:{message}".format(
            index=i,
            address=address,
            shift=shift,
            message=text))
