#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# $Id$
""" クラス FieldParserFactory の定義
"""

import dqutils.parser

class FieldParserFactory:
    """class FieldParserFactory
    
    論理設計的には Singleton であるべきなのだが Python における
    実装方式がわからない。
    """

    #m_parsers = {}

    def __init__(self):
        #self.m_parsers = {
        #    'bytes':parser.ParserByteField
        #    'bits':parser.ParserBitField,
        #}
        pass

    def get_field_parser(self, directive):
        """directive の中身次第で parser を返す。

        directive は辞書であり、次のキーを含むものとする

            index: 構造体レイアウトのベースアドレスからのオフセット byte 単位
            type:  構造体フィールドの型。以下のいずれかをサポート

            1) byte
            2) bit

            format: C 言語等の sprintf 関数の第一引数文字列と似たもの。Python ドキュメント参照。

        Example:
            {'index':0, 'type':'byte', 'size':2,    'format':'%04X', 'desc':'名前'}
            {'index':2, 'type':'bit',  'mask':0x3F, 'format':'%04X', 'desc':'レベル'}
        """
        ##assert type(directive) is type(dict)

        stindex = directive.get('index', -1)
        sttype = directive.get('type', '')
        stformat = directive.get('format', '')

        if sttype == 'byte':
            stn = directive.get('size', 0)
            return parser.ByteFieldParser(stindex, stformat, stn)
        elif sttype == 'bit':
            stmask = directive.get('mask', 0)
            return parser.BitFieldParser(stindex, stformat, stmask)
        else:
            return parser.ParserBase()

def test():
    #maker = FieldParserFactory()
    #
    #assert maker.get_field_parser('3byte')
    #assert maker.get_field_parser('2byte')
    #assert maker.get_field_parser('1byte')
    #assert maker.get_field_parser('bits')
    pass

if __name__ == '__main__':
    test()
