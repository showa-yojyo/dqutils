#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""dqutils.parser module
"""
from dqutils.bit import getbits, getbytes

class ParserBase:
    """class ParserBase
    
    各種 Parser クラスの基底クラス
    おそらくコンストラクタが必要となる
    """

    m_index = 0
    m_format = ''

    def __init__(self, index, format):
        """
        初期化関数
        index: 構造体レイアウトのベースアドレスからのオフセット。byte 単位
        format: 文字列フォーマット
        """
        self.m_index = index
        self.m_format = format

    def parse(self, bytes):
        """
        何もしない。オーバーライド専用メソッドとする。
        """
        return ''

class BitFieldParser(ParserBase):
    """class BitFieldParser
    
    C 言語で言う構造体ビットフィールドの数値を抽出する
    """

    m_mask = 0

    def __init__(self, index, format, mask):
        """
        初期化関数。
        index: 構造体レイアウトのベースアドレスからのオフセット。byte 単位
        format: 文字列フォーマット
        mask: ビットマスク
        """
        ParserBase.__init__(self, index, format)
        self.m_mask = mask

    def parse(self, bytes):
        return self.m_format % getbits(bytes, self.m_index, self.m_mask)

class ByteFieldParser(ParserBase):
    """class ByteFieldParser
    
    バイト境界にある整数倍サイズの数値を構造体フィールドとして抽出する
    """

    m_nbyte = 1

    def __init__(self, index, format, nbyte):
        """
        初期化関数。
        index: 構造体レイアウトのベースアドレスからのオフセット。byte 単位
        format: 文字列フォーマット
        nbyte: バイト長
        """
        ParserBase.__init__(self, index, format)
        self.m_nbyte = nbyte

    def parse(self, bytes):
        return self.m_format % getbytes(bytes, self.m_index, self.m_nbyte)


def _test():
    import doctest, parser
    return doctest.testmod(parser)

if __name__ == '__main__':
    _test()
