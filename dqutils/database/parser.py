#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""dqutils.database.parser - TBW
"""

from dqutils.database import table

def get_struct_info(structnode):
    """TEST"""

    cpuaddr = 0
    if structnode.hasAttribute('cpuaddress'):
        cpuaddr = get_int(structnode.getAttribute('cpuaddress'))

    recordsize = 0
    if structnode.hasAttribute('size'):
        recordsize = get_int(structnode.getAttribute('size'))

    recordnum = 0
    if structnode.hasAttribute('number'):
        recordnum = get_int(structnode.getAttribute('number'))

    return cpuaddr, recordsize, recordnum

def get_int(text):
    """Cast a text value to numeric."""

    if not text:
        return 0

    if text.startswith('0x'):
        return int(text, 16)  # 0x to hex
    else:
        return int(text, 10)  # decimal

# 実装しにくいので注意
def handle_member(mem):
    """<member> 要素の解析

    member 要素は属性しか持っていない。
    required な要素は name, offset, type だけ。
    """

    attrs = {}

    # required
    attr_name = mem.getAttribute('name')
    attr_type = mem.getAttribute('type')

    attrs['offset'] = get_int(mem.getAttribute('offset'))

    # optional
    attr_mask = get_int(mem.getAttribute('mask'))
    attr_format = mem.getAttribute('format')
    if attr_mask:
        attrs['mask'] = attr_mask
    if format:
        attrs['format'] = attr_format

    # pylint: disable=star-args
    return table.make_field(attr_name, attr_type, **attrs)
