# -*- coding: utf-8 -*-
"""dqutils.database.table (prototype)
"""

from dqutils.bit import getbits
from dqutils.bit import get_int
from dqutils.bit import readbytes
import dqutils.database.format

class Field(object):
    """構造体オブジェクト配列をデータベース的に捉えたときの
    カラム一個に相当するクラス。

    Attributes:
      name: string
      offset: int
      mask: int
      type: string
      default: any
    """

    # optparse のパクリ
    ATTRS = ['name', 'type', 'offset', 'mask', 'format']
    TYPES = ['byte', 'word', 'long', 'bits']

    def __init__(self, name, **attrs):
        """いろいろセットする"""
        self.name = name

        # Set all other attrs (action, type, etc.) from 'attrs' dict
        self._set_attrs(attrs)
        if not self.format:
            self.do_set_fmt()

    def __cmp__(self, other):
        """naive comparison"""
        sign = cmp(self.offset, other.offset)
        if sign != 0:
            return sign
        # マスク値を比較し、高位にある方を大とする。
        # XXX: ビットを下位から上位へ見ていく？
        return cmp(self.mask, other.mask)

    def __str__(self):
        """デバッグ用"""
        # TODO: 何を出力する？
        return self.name

    def _set_attrs(self, attrs):
        """メンバーデータをセット"""
        for i in self.ATTRS:
            if i in attrs:
                setattr(self, i, attrs[i])
                del attrs[i]  # 行儀が悪いが
        # TODO: 残りカスをチェック

    def do_set_fmt(self):
        """書式文字列をセット"""
        raise NotImplementedError("subclasses must implement")

    def process(self, chunk):
        """バイト塊を処理するメソッド"""
        return chunk

    def title(self):
        """フィールド名を返すだけ"""
        return self.name

class BitField(Field):
    """メンバーデータがビット列で表現されているものに対応する"""
    def __init__(self, name, **attrs):
        super().__init__(name, **attrs)

    def do_set_fmt(self):
        """書式文字列をセット"""
        self.format = '%X'

    def process(self, chunk):
        """バイト塊を処理するメソッド"""
        return self.format % getbits(chunk, self.offset, self.mask)

class ByteField(Field):
    """メンバーデータが 1byte で表現されているものに対応する"""
    def __init__(self, name, **attrs):
        super().__init__(name, **attrs)

    def do_set_fmt(self):
        """書式文字列をセット"""
        self.format = '%02X'

    def process(self, chunk):
        """バイト塊を処理するメソッド"""
        return self.format % get_int(chunk, self.offset, 1)

class WordField(Field):
    """メンバーデータが 2byte で表現されているものに対応する"""

    def __init__(self, name, **attrs):
        super().__init__(name, **attrs)

    def do_set_fmt(self):
        """書式文字列をセット"""
        self.format = '%04X'

    def process(self, chunk):
        """バイト塊を処理するメソッド"""
        return self.format % get_int(chunk, self.offset, 2)

class LongField(Field):
    """メンバーデータが 3byte で表現されているものに対応する"""

    def __init__(self, name, **attrs):
        super().__init__(name, **attrs)

    def do_set_fmt(self):
        """書式文字列をセット"""
        self.format = '%06X'

    def process(self, chunk):
        """バイト塊を処理するメソッド"""
        return self.format % get_int(chunk, self.offset, 3)

class BadFieldType(Exception):
    """フィールドタイプが不明な名前の場合の例外"""

    def __init__(self, bad_type):
        super().__init__()
        self.bad_type = bad_type

    def __str__(self):
        return "no such field type: {0}".format(self.bad_type)

def make_field(name, field_type, **kwargs):
    """Factory method"""

    if field_type in ('bit', 'bits'):
        return BitField(name, **kwargs)
    elif field_type in ('byte', '1byte'):
        return ByteField(name, **kwargs)
    elif field_type in ('word', '2byte'):
        return WordField(name, **kwargs)
    elif field_type in ('long', '3byte'):
        return LongField(name, **kwargs)
    else:
        raise BadFieldType(field_type)

class Table(object):
    """工事中"""

    # pylint: disable=too-many-arguments
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

    def add_field(self, name, **kwargs):
        """TBW"""
        self.field_list.append(make_field(name, **kwargs))

    def parse(self):
        """TBW"""

        if self.rom is None or self.reclen == 0:
            return

        saved_ptr = self.rom.tell()
        try:
            # locate the address of the array on ROM image
            self.rom.seek(self.romaddr)

            # setup table header information
            self.do_make_header()

            for _ in range(self.recnum):
                # obtain a byte sequence (list so far)
                chunk = self.rom.read(self.reclen)
                self.do_write_record(
                    [field.process(chunk) for field in self.field_list])
        finally:
            self.rom.seek(saved_ptr)

    def do_make_header(self):
        """テーブルヘッダを書式化して標準出力に出力する"""
        self.formatter.make_header([field.title() for field in self.field_list])

    def do_write_record(self, value_list):
        """レコード一行分を書式化して標準出力に出力する"""
        self.formatter.write_record(value_list)

    def sort_fields(self):
        """フィールドをそのアドレス位置の昇順でソート"""
        # TODO: Field.__cmp__ を実装しておくように
        self.field_list.sort()
