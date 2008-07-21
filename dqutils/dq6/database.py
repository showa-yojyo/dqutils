#! /usr/bin/env python
# -*- coding: utf-8 -*-
# $Id$
u"""dqutils.dq6.database モジュール

利用部と解析部との間にある
"""

from __future__ import with_statement
from dqutils.database import table
from dqutils.database.parser import get_struct_info, handle_member
from dqutils.address import conv_hi
from dqutils.dq6 import open_rom
from xml.dom.minidom import parse as parsexml
import sys
import mmap

__all__ = ['process_xml']

def process_xml(xml):
    u"""構造体情報を読み取る

    xml: XML ファイル
    """
    cpuaddr, recordsize, recordnum = 0, 0, 0
    fields = []
    with open(xml, 'r') as src:
        dom = parsexml(src)

        # handle <struct>
        structnode = dom.getElementsByTagName(u'struct')[0]
        cpuaddr, recordsize, recordnum = get_struct_info(structnode)

        for mem in structnode.getElementsByTagName(u'member'):
            fields.append(handle_member(mem))

    read_array(fields, cpuaddr, recordsize, recordnum)


def read_array(fields, cpuaddr, recordsize, recordnum):
    u"""構造体情報を読み取る

    """

    # create table
    with open_rom() as fin:
        rom = mmap.mmap(fin.fileno(), 0, access=mmap.ACCESS_READ)

        # TODO: convert address
        romaddr = conv_hi(cpuaddr)

        # [required] 構造体オブジェクト配列オブジェクト
        recordarray = table.Table(rom, romaddr, recordsize, recordnum)
        recordarray.field_list = fields

        # [optional] フィールドをそのアドレス位置の昇順でソート
        #recordarray.sort_fields()

        # [optional] 構造体オブジェクト配列を解析
        # CSV を標準出力に書き出す
        recordarray.parse()
