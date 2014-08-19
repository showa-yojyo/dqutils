#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""ドラクエ 5 小さいフォントの文字コード辞書

1. See dqviewer.exe <Sonitown, http://www.geocities.jp/sonitown> for the table of small font.
2. See dq3encode.c of dq_analyzer <Index of ~/s-endo, http://s-endo.skr.jp>

Both resources are free.
"""

charmap = {
    0x00:"",
    0x01:" ",
    0x02:"０",
    0x03:"１",
    0x04:"２",
    0x05:"３",
    0x06:"４",
    0x07:"５",
    0x08:"６",
    0x09:"７",
    0x0A:"８",
    0x0B:"９",
    0x0C:"Ｈ",
    0x0D:"Ｍ",
    0x0E:"Ｐ",
    0x0F:"Ｇ",
    0x10:"あ",
    0x11:"い",
    0x12:"う",
    0x13:"え",
    0x14:"お",
    0x15:"か",
    0x16:"き",
    0x17:"く",
    0x18:"け",
    0x19:"こ",
    0x1A:"さ",
    0x1B:"し",
    0x1C:"す",
    0x1D:"せ",
    0x1E:"そ",
    0x1F:"た",
    0x20:"ち",
    0x21:"つ",
    0x22:"て",
    0x23:"と",
    0x24:"な",
    0x25:"に",
    0x26:"ぬ",
    0x27:"ね",
    0x28:"の",
    0x29:"は",
    0x2A:"ひ",
    0x2B:"ふ",
    0x2C:"へ",
    0x2D:"ほ",
    0x2E:"ま",
    0x2F:"み",
    0x30:"む",
    0x31:"め",
    0x32:"も",
    0x33:"や",
    0x34:"ゆ",
    0x35:"よ",
    0x36:"ら",
    0x37:"り",
    0x38:"る",
    0x39:"れ",
    0x3A:"ろ",
    0x3B:"わ",
    0x3C:"を",
    0x3D:"ん",
    0x3E:"っ",
    0x3F:"ゃ",
    0x40:"ゅ",
    0x41:"ょ",
    0x42:"ア",
    0x43:"イ",
    0x44:"ウ",
    0x45:"エ",
    0x46:"オ",
    0x47:"カ",
    0x48:"キ",
    0x49:"ク",
    0x4A:"ケ",
    0x4B:"コ",
    0x4C:"サ",
    0x4D:"シ",
    0x4E:"ス",
    0x4F:"セ",
    0x50:"ソ",
    0x51:"タ",
    0x52:"チ",
    0x53:"ツ",
    0x54:"テ",
    0x55:"ト",
    0x56:"ナ",
    0x57:"ニ",
    0x58:"ヌ",
    0x59:"ネ",
    0x5A:"ノ",
    0x5B:"ハ",
    0x5C:"ヒ",
    0x5D:"フ",
    0x5E:"ヘ",
    0x5F:"ホ",
    0x60:"マ",
    0x61:"ミ",
    0x62:"ム",
    0x63:"メ",
    0x64:"モ",
    0x65:"ヤ",
    0x66:"ユ",
    0x67:"ヨ",
    0x68:"ラ",
    0x69:"リ",
    0x6A:"ル",
    0x6B:"レ",
    0x6C:"ロ",
    0x6D:"ワ",
    0x6E:"ヲ",
    0x6F:"ン",
    0x70:"ッ",
    0x71:"ャ",
    0x72:"ュ",
    0x73:"ョ",
    0x74:"ァ",
    0x75:"ィ",
    0x76:"ェ",
    0x77:"ォ",
    0x78:"ー",
    0x79:"？",
    0x7A:"！",
    0x7B:"▼",
    0x7C:"〓",
    0x7D:"→",
    0x7E:"[死]",
    0x7F:"[毒]",
    0x80:"[まひ]",
    0x81:"[呪]",
    0x82:"／",
    0x83:"゜",
    0x84:"゛",
    0x85:"：",
    0x86:"Ex",
    0x87:"Lv",
    0x88:"―",
    0x89:"＊",
    0x8A:"Ｅ",
    #0x8B:"┏",
    #0x8C:"┏",
    #0x8D:"━",
    #0x8E:"┃",
    #0x8F:"┠",
    #0x90:"─",
    #0x91:"┃E",
    #0x92:"━",
    #0x93:"━",
    #0x94:"─",
    #0x95:"─",
    #0x96:"〓",
    #0x97:"┗",
    #0x98:"━",
    #0x99:"┗",
    0x9A:"。",
    0x9B:"．",
    0x9C:"「",
    0x9D:"…",
    0x9E:"ど",
    0x9F:"．",
    0xA0:"Ａ",
    0xA1:"Ｂ",
    0xA2:"Ｃ",
    0xA3:"Ｄ",
    0xA4:"Ｅ",
    0xA5:"Ｆ",
    0xA6:"Ｇ",
    0xA7:"Ｈ",
    0xA8:"Ｉ",
    0xA9:"Ｊ",
    0xAA:"Ｋ",
    0xAB:"Ｌ",
    0xAC:"Ｍ",
    0xAD:"Ｎ",
    0xAE:"Ｏ",
    0xAF:"Ｐ",
    #0xB0:"[B0]",
    #0xB1:"[B1]",
    #0xB2:"[B2]",
    #0xB3:"[B3]",
    #0xB4:"[B4]",
    #0xB5:"[B5]",
    #0xB6:"[B6]",
    #0xB7:"[B7]",
    #0xB8:"[B8]",
    #0xB9:"[B9]",
    #0xBA:"[BA]",
    #0xBB:"[BB]",
    #0xBC:"[BC]",
    #0xBD:"[BD]",
    #0xBE:"[BE]",
    #0xBF:"[BF]",
    #0xC0:"[C0]",
    #0xC1:"[C1]",
    #0xC2:"[C2]",
    #0xC3:"[C3]",
    #0xC4:"[C4]",
    #0xC5:"[C5]",
    #0xC6:"[C6]",
    #0xC7:"[C7]",
    #0xC8:"[C8]",
    #0xC9:"[C9]",
    #0xCA:"[CA]",
    #0xCB:"[CB]",
    #0xCC:"[CC]",
    #0xCD:"[CD]",
    #0xCE:"[CE]",
    #0xCF:"[CF]",
    #0xD0:"[D0]",
    #0xD1:"[D1]",
    #0xD2:"[D2]",
    #0xD3:"[D3]",
    #0xD4:"[D4]",
    #0xD5:"[D5]",
    #0xD6:"[D6]",
    #0xD7:"[D7]",
    #0xD8:"[D8]",
    #0xD9:"[D9]",
    #0xDA:"[DA]",
    #0xDB:"[DB]",
    #0xDC:"[DC]",
    #0xDD:"[DD]",
    #0xDE:"[DE]",
    #0xDF:"[DF]",
    #0xE0:"[E0]",
    #0xE1:"[E1]",
    #0xE2:"[E2]",
    #0xE3:"[E3]",
    #0xE4:"[E4]",
    #0xE5:"[E5]",
    #0xE6:"[E6]",
    #0xE7:"[E7]",
    #0xE8:"[E8]",
    #0xE9:"[E9]",
    #0xEA:"[EA]",
    #0xEB:"[EB]",
    #0xEC:"[EC]",
    #0xED:"[ED]",
    #0xEE:"[EE]",
    #0xEF:"[EF]",
    #0xF0:"[F0]",
    #0xF1:"[F1]",
    #0xF2:"[F2]",
    #0xF3:"[F3]",
    #0xF4:"[F4]",
    #0xF5:"[F5]",
    #0xF6:"[F6]",
    #0xF7:"[F7]",
    #0xF8:"[F8]",
    #0xF9:"[F9]",
    #0xFA:"[FA]",
    #0xFB:"[FB]",
    #0xFC:"[FC]",
    #0xFD:"[FD]",
    #0xFE:"[FE]",
    #0xFF:"[FF]",
}

def process_dakuten(text):
    if "゜" in text:
        text = text.replace('゜は', 'ぱ').\
                    replace('゜ひ', 'ぴ').\
                    replace('゜ふ', 'ぷ').\
                    replace('゜へ', 'ぺ').\
                    replace('゜ほ', 'ぽ').\
                    replace('゜ハ', 'パ').\
                    replace('゜ヒ', 'ピ').\
                    replace('゜フ', 'プ').\
                    replace('゜ヘ', 'ペ').\
                    replace('゜ホ', 'ポ')
    if "゛" in text:
        text = text.replace('゛か', 'が').\
                    replace('゛き', 'ぎ').\
                    replace('゛く', 'ぐ').\
                    replace('゛け', 'げ').\
                    replace('゛こ', 'ご').\
                    replace('゛さ', 'ざ').\
                    replace('゛し', 'じ').\
                    replace('゛す', 'ず').\
                    replace('゛せ', 'ぜ').\
                    replace('゛そ', 'ぞ').\
                    replace('゛た', 'だ').\
                    replace('゛ち', 'ぢ').\
                    replace('゛つ', 'づ').\
                    replace('゛て', 'で').\
                    replace('゛と', 'ど').\
                    replace('゛は', 'ば').\
                    replace('゛ひ', 'び').\
                    replace('゛ふ', 'ぶ').\
                    replace('゛へ', 'べ').\
                    replace('゛ほ', 'ぼ').\
                    replace('゛カ', 'ガ').\
                    replace('゛キ', 'ギ').\
                    replace('゛ク', 'グ').\
                    replace('゛ケ', 'ゲ').\
                    replace('゛コ', 'ゴ').\
                    replace('゛サ', 'ザ').\
                    replace('゛シ', 'ジ').\
                    replace('゛ス', 'ズ').\
                    replace('゛セ', 'ゼ').\
                    replace('゛ソ', 'ゾ').\
                    replace('゛タ', 'ダ').\
                    replace('゛チ', 'ヂ').\
                    replace('゛ツ', 'ヅ').\
                    replace('゛テ', 'デ').\
                    replace('゛ト', 'ド').\
                    replace('゛ハ', 'バ').\
                    replace('゛ヒ', 'ビ').\
                    replace('゛フ', 'ブ').\
                    replace('゛ヘ', 'ベ').\
                    replace('゛ホ', 'ボ')
    return text

def print_charmap():
    """Print the symbol table.

    It is much faster to open this file in the text editor.
    """

    for i, v in charmap.items():
        print('{0:02X}:{1}'.format(i, v))

if __name__ == "__main__":
    print_charmap()
