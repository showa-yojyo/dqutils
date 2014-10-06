# -*- coding: utf-8 -*-
""" dqutils package - dqutils.database __init__ module
"""

from dqutils.database.table import Table
from dqutils.database.parser import get_struct_info
from dqutils.database.parser import handle_member
from dqutils.address import conv_hi
from dqutils.address import conv_lo
from dqutils.rom_image import RomImage
from xml.dom.minidom import parse as parse_xml

def process_xml(context, xml):
    """構造体情報を読み取る

    xml: XML ファイル
    """
    cpuaddr, recordsize, recordnum = 0, 0, 0
    with open(xml, 'r', encoding='utf-8') as src:
        dom = parse_xml(src)

        # handle <struct>
        node = dom.getElementsByTagName('struct')[0]
        cpuaddr, record_size, record_num = get_struct_info(node)
        read_array(
            context, 
            [handle_member(i) for i in node.getElementsByTagName('member')],
            cpuaddr,
            record_size,
            record_num)

def read_array(context, fields, cpuaddr, record_size, record_num):
    """構造体情報を読み取る

    """

    # Test preconditions.
    assert "title" in context
    assert "mapper" in context

    mapper = context["mapper"]
    if mapper == 'HiROM':
        from_cpu = conv_hi
    elif mapper == 'LoROM':
        from_cpu = conv_lo

    # create table
    with RomImage(context["title"]) as mem:
        # [required] 構造体オブジェクト配列オブジェクト
        record_seq = Table(mem, from_cpu(cpuaddr), record_size, record_num)
        record_seq.field_list = fields

        # [optional] フィールドをそのアドレス位置の昇順でソート
        #record_seq.sort_fields()

        # [optional] 構造体オブジェクト配列を解析
        # CSV を標準出力に書き出す
        record_seq.parse()
