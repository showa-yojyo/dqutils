#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""dqutils.database.format -- (prototype)
"""

class TableFormatter(object):
    """テーブルを書式化して出力するための抽象クラス。
    クラス Table がこのサブクラスのうちのひとつを用いる。
    ちなみにデフォルトでは CSVFormatter を使う。

    属性の説明:
      [TODO]
    """

    def __init__(self):
        pass

    def make_header(self, title_list):
        """テーブルヘッダを書式化して標準出力に出力する"""
        raise NotImplementedError("subclasses must implement")

    def write_record(self, value_list):
        """レコード一行分を書式化して標準出力に出力する"""
        raise NotImplementedError("subclasses must implement")

class CSVFormatter(TableFormatter):
    """ROM を parse しながら構造体オブジェクト配列を CSV として出力する

    属性の説明:
      sep  CSV におけるセパレータ文字列。デフォルトはコロン。
    """

    def __init__(self, sep=':'):
        TableFormatter.__init__(self)
        self.sep = sep

    def make_header(self, title_list):
        """CSV のヘッダ部分を出力する"""
        print(self.sep.join(title_list))

    def write_record(self, value_list):
        """CSV 形式でレコード一行分を標準出力に出力する"""
        print(self.sep.join(value_list))

# 以下未実装

#class XMLFormatter(TableFormatter):
#    """ROM を parse しながら構造体オブジェクト配列を XML として出力する
#    """
#    def __init__(self):
#        super().__init__()
#
#class ExcelFormatter(TableFormatter):
#    """ROM を parse しながら構造体オブジェクト配列を
#    Excel スプレッドシートに出力する。
#
#    win32com モジュールを利用するので、Windows 以外では使えない。
#    （だからこのファイルにコードを書いてはいけない）
#    """
#    def __init__(self):
#        super().__init__()
#        # TODO:
#        #import win32com.client
#        #excel = win32com.client.Dispatch('Excel.Application')
#        #...
