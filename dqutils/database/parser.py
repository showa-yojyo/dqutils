# -*- coding: utf-8 -*-
"""dqutils.database.parser - TBW
"""
from dqutils.database.field import make_field

def get_struct_info(node):
    """Returns the information in order to retrieve data from ROM.

    Args:
      structnore (xmlnode): The `<struct>` node in the XML file.

    Returns:
      A tuple of (cpu address, record size, record count).
    """

    cpu_addr = 0
    if node.hasAttribute('cpuaddress'):
        cpu_addr = get_int(node.getAttribute('cpuaddress'))

    record_size = 0
    if node.hasAttribute('size'):
        record_size = get_int(node.getAttribute('size'))

    record_num = 0
    if node.hasAttribute('number'):
        record_num = get_int(node.getAttribute('number'))

    return cpu_addr, record_size, record_num

def get_int(text):
    """Cast a text value to a numeric value.

    Args:
      text (string): A text which represents an decimal or hexadecimal
        integer.

    Returns:
      An integer.
    """

    if not text:
        return 0

    if text.startswith('0x'):
        return int(text, 16)
    else:
        return int(text, 10)

def get_member_info(node):
    """Returns information of a member or field from a member element.

    A `member` element must have three attributes: `name`, `offset`,
    and `type`. Other attributes such as `mask` or `format' are optional.

    Args:
      node: A `<member>` DOM element.

    Returns:
      (AbstractField): An instance which has information of the member or
        field.
    """

    attrs = {}

    attr_name = node.getAttribute('name')
    attr_type = node.getAttribute('type')
    attrs['offset'] = get_int(node.getAttribute('offset'))

    attr_mask = get_int(node.getAttribute('mask'))
    if attr_mask:
        attrs['mask'] = attr_mask

    attr_format = node.getAttribute('format')
    if format:
        attrs['format'] = attr_format

    # pylint: disable=star-args
    return make_field(attr_name, attr_type, **attrs)
