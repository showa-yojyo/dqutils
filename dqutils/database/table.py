#! /usr/bin/env python
# -*- coding: utf-8 -*-
# $Id$
u"""dqutils.database.table モジュール

試作版だよ
"""

from dqutils.bit import getbits, getbytes, readbytes
from dqutils.database import format as fmt
import types

# for 'import *'
__all__ = ['Field',
           'make_field',
           'Table',
           ]

class Field:
    u"""構造体オブジェクト配列をデータベース的に捉えたときの
    カラム一個に相当するクラス。

    Attributes:
      name: string
      offset: int
      mask: int
      type: string
      default: any
    """

    # optparse のパクリ
    ATTRS = ['name','type','offset','mask','format']
    TYPES = ['byte','word','long','bits']

    def __init__(self, name, *opts, **attrs):
        u"""いろいろセットする"""
        self.name = name

        # Set all other attrs (action, type, etc.) from 'attrs' dict
        self._set_attrs(attrs)
        if not hasattr(self, 'format'):
            self.do_set_fmt()

        assert self.format

    def __cmp__(self, other):
        u"""naive comparison"""
        sign = cmp(self.offset, other.offset)
        if sign != 0:
            return sign
        # マスク値を比較し、高位にある方を大とする。
        # XXX: ビットを下位から上位へ見ていく？
        return cmp(self.mask, other.mask)

    def __str__(self):
        u"""デバッグ用"""
        # TODO: 何を出力する？
        return self.name

    def _set_attrs(self, attrs):
        u"""メンバーデータをセット"""
        for a in self.ATTRS:
            if attrs.has_key(a):
                setattr(self, a, attrs[a])
                del attrs[a]  # 行儀が悪いが
        # TODO: 残りカスをチェック

    def do_set_fmt(self):
        u"""書式文字列をセット"""
        raise NotImplementedError, "subclasses must implement"

    def process(self, chunk):
        u"""バイト塊を処理するメソッド"""
        return ''

    def title(self):
        u"""フィールド名を返すだけ"""
        return self.name


class BitField(Field):
    u"""メンバーデータがビット列で表現されているものに対応する"""
    def __init__(self, name, *opts, **attrs):
        Field.__init__(self, name, *opts, **attrs)

    def do_set_fmt(self):
        u"""書式文字列をセット"""
        self.format = '%X'

    def process(self, chunk):
        u"""バイト塊を処理するメソッド"""
        return self.format % getbits(chunk, self.offset, self.mask)


class ByteField(Field):
    u"""メンバーデータが 1byte で表現されているものに対応する"""
    def __init__(self, name, *opts, **attrs):
        Field.__init__(self, name, *opts, **attrs)

    def do_set_fmt(self):
        u"""書式文字列をセット"""
        self.format = '%02X'

    def process(self, chunk):
        u"""バイト塊を処理するメソッド"""
        return self.format % getbytes(chunk, self.offset, 1)


class WordField(Field):
    u"""メンバーデータが 2byte で表現されているものに対応する"""
    def __init__(self, name, *opts, **attrs):
        Field.__init__(self, name, *opts, **attrs)

    def do_set_fmt(self):
        u"""書式文字列をセット"""
        self.format = '%04X'

    def process(self, chunk):
        u"""バイト塊を処理するメソッド"""
        return self.format % getbytes(chunk, self.offset, 2)


class LongField(Field):
    u"""メンバーデータが 3byte で表現されているものに対応する"""
    def __init__(self, name, *opts, **attrs):
        Field.__init__(self, name, *opts, **attrs)

    def do_set_fmt(self):
        u"""書式文字列をセット"""
        self.format = '%06X'

    def process(self, chunk):
        u"""バイト塊を処理するメソッド"""
        return self.format % getbytes(chunk, self.offset, 3)


class BadFieldType(Exception):
    u"""フィールドタイプが不明な名前の場合の例外"""

    def __init__(self, type):
        self.type = type

    def __str__(self):
        return "no such field type: %s" % self.type


def make_field(name, type, *args, **kwargs):
    u"""Factory method"""
    if type in (u'bit', u'bits'):
        return BitField(name, *args, **kwargs)
    elif type in (u'byte', u'1byte'):
        return ByteField(name, *args, **kwargs)
    elif type in (u'word', u'2byte'):
        return WordField(name, *args, **kwargs)
    elif type in (u'long', u'3byte'):
        return LongField(name, *args, **kwargs)
    else:
        raise BadFieldType(type)


class Table:
    u"""工事中"""

    def __init__(self, 
                 rom=None,
                 romaddr=0,
                 reclen=0,
                 recnum=0,
                 formatter=None):
        self.field_list = []
        self.rom = rom  # これ作っていなかった
        self.romaddr = romaddr  # 配列先頭の ROM アドレス
        self.reclen = reclen # sizeof(struct S)
        self.recnum = recnum # オブジェクト個数 i.e. レコード個数
        if formatter is None:
            formatter = fmt.CSVFormatter()
        self.formatter = formatter

    def add_field(self, name, *args, **kwargs):
        self.field_list.append(make_field(name, *args, **kwargs))

    def parse(self):
        if self.rom is None or self.reclen == 0:
            return

        # locate the address of the array on ROM image
        self.rom.seek(self.romaddr)  # TODO: seekptr を元に戻す

        # setup table header information
        self.do_make_header()

        for i in xrange(self.recnum):
            # obtain a byte sequence (list so far)
            chunk = readbytes(self.rom, self.reclen)
            self.do_write_record([field.process(chunk) for field in self.field_list])

    def do_make_header(self):
        u"""テーブルヘッダを書式化して標準出力に出力する"""
        self.formatter.make_header([field.title() for field in self.field_list])

    def do_write_record(self, value_list):
        u"""レコード一行分を書式化して標準出力に出力する"""
        self.formatter.write_record(value_list)

    def sort_fields(self):
        u"""フィールドをそのアドレス位置の昇順でソート"""
        # Field.__cmp__ を実装しておくように
        self.field_list.sort()

