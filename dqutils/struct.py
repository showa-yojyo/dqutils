#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# $Id$
"""ドラクエのロムイメージに含まれる構造体型配列をテキスト化して出力する
"""

import sys
import ConfigParser
import dqutils.factory
from dqutils.bit import getbits, getbytes, readbytes

CFGSEP = ':'    # a colon

def parse_structs(rompath, confpath):
    """
    TODO: 関数名をなんとかする
    """
    # 必ず標準出力に出力する
    stream = sys.stdout

    # conf ファイルを読み出す
    conf = read_config(confpath)

    # ロムイメージをバイナリモードで開く
    fp = open(rompath, 'rb')

    # 基本情報を得る
    romaddr, sizeof, nobj = rominfo(conf)

    # TODO: ここが美しくない
    # ヘッダ列とフィールド解析オブジェクトリストを同時に作成する
    header, parsers = make_parsers(conf)

    # まずはヘッダ列を出力する
    stream.write(CFGSEP.join(header))
    stream.write("\n")

    # 一気にドラクエオブジェクトをテキスト化して出力する
    for counter in range(0, nobj):
        fp.seek(romaddr + counter * sizeof)
        write_object(stream, parsers, [ord(i) for i in fp.read(sizeof)])
        stream.write("\n")

    fp.close()

def read_config(confpath):
    """ConfigParser テスト
    """
    conf = ConfigParser.ConfigParser()
    conf.readfp(open(confpath))
    return conf

def rominfo(conf):
    return int(conf.get("object type", "romaddress"), 16), int(conf.get("object type", "sizeof"), 16), int(conf.get("object type", "number"), 16)

def make_parsers(conf):
    """
    parser リストを出力
    """
    sect = "object layout"
    maker = factory.FieldParserFactory()
    header = []
    parsers = []

    for opt in sorted(conf.options(sect)):
        directive = conf.get(sect, opt)
        # オプションの右側に書いてあるものは辞書と仮定する
        if directive.startswith('{') and directive.endswith('}'):
            directive = eval(directive)

            # これはヘッダとなる
            header.append(directive.get('name', '-'))
            parsers.append(maker.get_field_parser(directive))

    return header, parsers

def write_object(stream, parsers, bytes):
    """
    stream に bytes を解析した結果を出力する。
    解析器となるのが parsers 各オブジェクトだ。
    """
    for parser in parsers:
        stream.write(parser.parse(bytes))
        stream.write(CFGSEP)


class StructMemInfo:
    """Information of a member of a struct.
    """
    # メンバー情報
    # memname            as string (optional)
    # offset (aka index) as int
    # mask               as int
    # format             as string (optional)
    #
    # オフセット位置の相対関係がそのまま比較関数になる

    def __init__(self, *args, **kwargs):
        """TODO"""

        self.m_name   = kwargs.get('name', '')

        # offset
        if 'index' in kwargs:
            # index is a synonym of offset
            self.m_offset = kwargs.get('index')
        else:
            self.m_offset = kwargs.get('offset', 0)

        # field alignment
        if 'type' in kwargs:
            field_type = kwargs['type']
            if field_type == 'byte' and 'size' in kwargs:
                self.m_type = field_type
                self.m_size = kwargs['size']
            elif field_type == 'bit':
                self.m_type = field_type
                self.m_mask = kwargs.get('mask', 0xFFFF)

        # format-string
        self.m_format = kwargs.get('format', '%X')

    def __repr__(self):
        """Dump the class data."""
        return '(%s, 0x%04X, 0x%06X, "%s")' % (self.m_name, self.m_offset, self.m_mask, self.m_format)


    def get_value(self, chunk):
        """Return the value of the member data"""
        #print 'chunk:', chunk

        if self.m_type == 'byte':
            value = getbytes(chunk, self.m_offset, self.m_size)
        elif self.m_type == 'bit':
            value = getbits(chunk, self.m_offset, self.m_mask)

        return value


class StructInfo:
    """Information of a struct.
    """

    # 構造体情報
    # structname         as string (optional)
    # base location      as cpuaddr
    # sizeof             as int
    # number             as int
    # meminfo[]          as メンバー情報

    def __init__(self, *args, **kwargs):
        """TODO"""
        self.m_name = kwargs.get('name', '')
        self.m_loc  = kwargs.get('location', 0)
        self.m_size = kwargs.get('sizeof', 1)
        self.m_len  = kwargs.get('len', 1)
        self.m_members = kwargs.get('members', [])


    def __repr__(self):
        """Dump the class data."""

        rep = 'Name: %s\nBase Address: $%06X\nSizeof: $%04X\nArray Length: $%X' % (
            self.m_name, self.m_loc, self.m_size, self.m_len)
        if self.m_members:
            rep += '\nMembers:\n'
            for m in self.m_members:
                rep += m.__repr__()
                rep += '\n'
        return rep


    def parse(self, rom):
        """Parse ROM image and read member data"""
        # First locate the address of the array on ROM image
        rom.seek(self.m_loc)

        # traverse
        sizeof = self.m_size
        length = self.m_len
        members = self.m_members
        if sizeof == 0 or length == 0 or not members:
            return

        # TODO: write column header if possible
        print '(COLUMN HEADER LINE COMES HERE)'
        colheader = ['ID']
        for col, mem in enumerate(members):
            colheader.append(mem.m_name.decode('utf-8'))

        print CFGSEP.join(colheader)

        for id in xrange(length):
            # obtain a byte sequence (list so far)
            chunk = readbytes(rom, sizeof)

            columns = []
            for col, mem in enumerate(members):
                columns.append(mem.m_format % mem.get_value(chunk))

            print '%04X%s%s' % (id, CFGSEP, CFGSEP.join(columns))


def demo():
    """Demonstration."""

    # ROM 不確定
    # name
    # HiROM/LoROM
    #
    # conf からファイルが開ければよいことにする
    info = dict(name=u'Name ID', offset=0, format='TEXT[%04X]')
    meminfo = StructMemInfo(**info)

    info = dict(name=u'最大 HP', offset=0x22, mask = 0xFFFF, format='%4d')
    mhp = StructMemInfo(**info)

    parse_start(0x020000, 0x25, 0xA0, [meminfo, mhp])


def fromconf(f):
    """TODO"""
    conf = read_config(f)
    romaddr, sizeof, length = rominfo(conf)

    sect = 'object layout'
    members = []
    for opt in sorted(conf.options(sect)):
        directive = conf.get(sect, opt)
        if directive.startswith('{') and directive.endswith('}'):
            # dict
            members.append(StructMemInfo(**eval(directive)))

    parse_start(romaddr, sizeof, length, members)


def parse_start(romaddr, sizeof, length, members):
    """TODO"""
    structinfo = StructInfo(
        name     = u'モンスターデータ列', 
        location = romaddr,
        sizeof   = sizeof,
        len      = length,
        members  = members,
        )

    #print structinfo

    from dqutils.dq3 import open_rom
    fin = open_rom()
    import mmap
    rom = mmap.mmap(fin.fileno(), 0, access = mmap.ACCESS_READ)
    structinfo.parse(rom)
    rom.close()
    fin.close()


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        fromconf(sys.argv[1])
    else:
        demo()
