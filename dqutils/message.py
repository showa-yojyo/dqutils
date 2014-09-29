# -*- coding: utf-8 -*-

"""dqutils.message module
"""

from dqutils.string import get_text
from dqutils.string import get_hex
from dqutils.string import enum_string
from dqutils.romimage import RomImage
from dqutils.message_decoder import MessageDecoder
from array import array

def enum_battle(context, first=None, last=None):
    """Generate battle message data.

    Message data that indices in [`first`, `last`) will be output.

    Args:
      context: TBW
      first: The first index of the range you want.
      last: The last index + 1 of the range you want.

    Yields:
      TBW
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

    assert "addr_message" in context
    addr = context["addr_message"]

    delims = context["delimiters"]
    assert delims is None or isinstance(delims, bytes)

    with RomImage(context["title"]) as mem:
        for i in enum_string(mem, first, last, addr, delims):
            yield i

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

def enum_scenario(context, first=None, last=None):
    """Generate scenario message data.

    Message data that indices in [`first`, `last`) will be output.

    Args:
      context: TBW
      first: The first index of the range you want.
      last: The last index + 1 of the range you want.

    Yields:
      address, shift, code_seq
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
        decoder = MessageDecoder(**context)
        decoder.setup(mem)
        for message in decoder.enumerate(mem, first, last):
            yield message

def print_scenario(context, first=None, last=None):
    """Print message data to sys.stdout.

    Message data that indices in [`first`, `last`) will be output.

    Args:
      context: TBW
      first: The first index of the range you want.
      last: The last index + 1 of the range you want.

    Returns:
      None.
    """

    charmap = context["charmap"]
    assert charmap is None or isinstance(charmap, dict)

    delims = context["delimiters"]
    assert delims is None or isinstance(delims, array)

    for i, item in enumerate(enum_scenario(context, first, last)):
        address, shift, code_seq = item
        text = get_text(code_seq, charmap, delims)
        print("{index:04X}:{address:06X}:{shift:02X}:{message}".format(
            index=i,
            address=address,
            shift=shift,
            message=text))
