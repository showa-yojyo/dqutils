#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""dqutils.database.parser モジュール

利用部と解析部との間にある
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
    name = mem.getAttribute('name')
    type = mem.getAttribute('type')

    attrs['offset'] = get_int(mem.getAttribute('offset'))

    # optional
    mask = get_int(mem.getAttribute('mask'))
    format = mem.getAttribute('format')
    if mask:
        attrs['mask'] = mask
    if format:
        attrs['format'] = format

    return table.make_field(name, type, **attrs)
