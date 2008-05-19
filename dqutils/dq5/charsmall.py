#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# $Id$
r"""ドラクエ 5 小さいフォントの文字コード辞書

See dqviewer.exe for the table of small font, as well as dq3encode.c of 
dq_analyzer, which are free software distributed in Sonitown 
(http://www.geocities.jp/sonitown) and Index of ~/s-endo 
(http://s-endo.skr.jp), respectively.
"""

charmap = {
    0x00:u"",
    0x01:u" ",
    0x02:u"０",
    0x03:u"１",
    0x04:u"２",
    0x05:u"３",
    0x06:u"４",
    0x07:u"５",
    0x08:u"６",
    0x09:u"７",
    0x0A:u"８",
    0x0B:u"９",
    0x0C:u"Ｈ",
    0x0D:u"Ｍ",
    0x0E:u"Ｐ",
    0x0F:u"Ｇ",
    0x10:u"あ",
    0x11:u"い",
    0x12:u"う",
    0x13:u"え",
    0x14:u"お",
    0x15:u"か",
    0x16:u"き",
    0x17:u"く",
    0x18:u"け",
    0x19:u"こ",
    0x1A:u"さ",
    0x1B:u"し",
    0x1C:u"す",
    0x1D:u"せ",
    0x1E:u"そ",
    0x1F:u"た",
    0x20:u"ち",
    0x21:u"つ",
    0x22:u"て",
    0x23:u"と",
    0x24:u"な",
    0x25:u"に",
    0x26:u"ぬ",
    0x27:u"ね",
    0x28:u"の",
    0x29:u"は",
    0x2A:u"ひ",
    0x2B:u"ふ",
    0x2C:u"へ",
    0x2D:u"ほ",
    0x2E:u"ま",
    0x2F:u"み",
    0x30:u"む",
    0x31:u"め",
    0x32:u"も",
    0x33:u"や",
    0x34:u"ゆ",
    0x35:u"よ",
    0x36:u"ら",
    0x37:u"り",
    0x38:u"る",
    0x39:u"れ",
    0x3A:u"ろ",
    0x3B:u"わ",
    0x3C:u"を",
    0x3D:u"ん",
    0x3E:u"っ",
    0x3F:u"ゃ",
    0x40:u"ゅ",
    0x41:u"ょ",
    0x42:u"ア",
    0x43:u"イ",
    0x44:u"ウ",
    0x45:u"エ",
    0x46:u"オ",
    0x47:u"カ",
    0x48:u"キ",
    0x49:u"ク",
    0x4A:u"ケ",
    0x4B:u"コ",
    0x4C:u"サ",
    0x4D:u"シ",
    0x4E:u"ス",
    0x4F:u"セ",
    0x50:u"ソ",
    0x51:u"タ",
    0x52:u"チ",
    0x53:u"ツ",
    0x54:u"テ",
    0x55:u"ト",
    0x56:u"ナ",
    0x57:u"ニ",
    0x58:u"ヌ",
    0x59:u"ネ",
    0x5A:u"ノ",
    0x5B:u"ハ",
    0x5C:u"ヒ",
    0x5D:u"フ",
    0x5E:u"ヘ",
    0x5F:u"ホ",
    0x60:u"マ",
    0x61:u"ミ",
    0x62:u"ム",
    0x63:u"メ",
    0x64:u"モ",
    0x65:u"ヤ",
    0x66:u"ユ",
    0x67:u"ヨ",
    0x68:u"ラ",
    0x69:u"リ",
    0x6A:u"ル",
    0x6B:u"レ",
    0x6C:u"ロ",
    0x6D:u"ワ",
    0x6E:u"ヲ",
    0x6F:u"ン",
    0x70:u"ッ",
    0x71:u"ャ",
    0x72:u"ュ",
    0x73:u"ョ",
    0x74:u"ァ",
    0x75:u"ィ",
    0x76:u"ェ",
    0x77:u"ォ",
    0x78:u"ー",
    0x79:u"？",
    0x7A:u"！",
    0x7B:u"▼",
    0x7C:u"〓",
    0x7D:u"→",
    0x7E:u"[死]",
    0x7F:u"[毒]",
    0x80:u"[まひ]",
    0x81:u"[呪]",
    0x82:u"／",
    0x83:u"゜",
    0x84:u"゛",
    0x85:u"：",
    0x86:u"Ex",
    0x87:u"Lv",
    0x88:u"―",
    0x89:u"＊",
    0x8A:u"Ｅ",
    #0x8B:u "┏",
    #0x8C:u"┏",
    #0x8D:u"━",
    #0x8E:u"┃",
    #0x8F:u"┠",
    #0x90:u"─",
    #0x91:u"┃E",
    #0x92:u"━",
    #0x93:u"━",
    #0x94:u"─",
    #0x95:u"─",
    #0x96:u"〓",
    #0x97:u"┗",
    #0x98:u"━",
    #0x99:u"┗",
    0x9A:u"。",
    0x9B:u"．",
    0x9C:u"「",
    0x9D:u"…",
    0x9E:u"ど",
    0x9F:u"．",
    0xA0:u"Ａ",
    0xA1:u"Ｂ",
    0xA2:u"Ｃ",
    0xA3:u"Ｄ",
    0xA4:u"Ｅ",
    0xA5:u"Ｆ",
    0xA6:u"Ｇ",
    0xA7:u"Ｈ",
    0xA8:u"Ｉ",
    0xA9:u"Ｊ",
    0xAA:u"Ｋ",
    0xAB:u"Ｌ",
    0xAC:u"Ｍ",
    0xAD:u"Ｎ",
    0xAE:u"Ｏ",
    0xAF:u"Ｐ",
    #0xB0:u"[B0]",
    #0xB1:u"[B1]",
    #0xB2:u"[B2]",
    #0xB3:u"[B3]",
    #0xB4:u"[B4]",
    #0xB5:u"[B5]",
    #0xB6:u"[B6]",
    #0xB7:u"[B7]",
    #0xB8:u"[B8]",
    #0xB9:u"[B9]",
    #0xBA:u"[BA]",
    #0xBB:u"[BB]",
    #0xBC:u"[BC]",
    #0xBD:u"[BD]",
    #0xBE:u"[BE]",
    #0xBF:u"[BF]",
    #0xC0:u"[C0]",
    #0xC1:u"[C1]",
    #0xC2:u"[C2]",
    #0xC3:u"[C3]",
    #0xC4:u"[C4]",
    #0xC5:u"[C5]",
    #0xC6:u"[C6]",
    #0xC7:u"[C7]",
    #0xC8:u"[C8]",
    #0xC9:u"[C9]",
    #0xCA:u"[CA]",
    #0xCB:u"[CB]",
    #0xCC:u"[CC]",
    #0xCD:u"[CD]",
    #0xCE:u"[CE]",
    #0xCF:u"[CF]",
    #0xD0:u"[D0]",
    #0xD1:u"[D1]",
    #0xD2:u"[D2]",
    #0xD3:u"[D3]",
    #0xD4:u"[D4]",
    #0xD5:u"[D5]",
    #0xD6:u"[D6]",
    #0xD7:u"[D7]",
    #0xD8:u"[D8]",
    #0xD9:u"[D9]",
    #0xDA:u"[DA]",
    #0xDB:u"[DB]",
    #0xDC:u"[DC]",
    #0xDD:u"[DD]",
    #0xDE:u"[DE]",
    #0xDF:u"[DF]",
    #0xE0:u"[E0]",
    #0xE1:u"[E1]",
    #0xE2:u"[E2]",
    #0xE3:u"[E3]",
    #0xE4:u"[E4]",
    #0xE5:u"[E5]",
    #0xE6:u"[E6]",
    #0xE7:u"[E7]",
    #0xE8:u"[E8]",
    #0xE9:u"[E9]",
    #0xEA:u"[EA]",
    #0xEB:u"[EB]",
    #0xEC:u"[EC]",
    #0xED:u"[ED]",
    #0xEE:u"[EE]",
    #0xEF:u"[EF]",
    #0xF0:u"[F0]",
    #0xF1:u"[F1]",
    #0xF2:u"[F2]",
    #0xF3:u"[F3]",
    #0xF4:u"[F4]",
    #0xF5:u"[F5]",
    #0xF6:u"[F6]",
    #0xF7:u"[F7]",
    #0xF8:u"[F8]",
    #0xF9:u"[F9]",
    #0xFA:u"[FA]",
    #0xFB:u"[FB]",
    #0xFC:u"[FC]",
    #0xFD:u"[FD]",
    #0xFE:u"[FE]",
    #0xFF:u"[FF]",
}


def process_dakuten(text):
    if u"゜" in text:
        text = text.replace(u'゜は', u'ぱ').\
                    replace(u'゜ひ', u'ぴ').\
                    replace(u'゜ふ', u'ぷ').\
                    replace(u'゜へ', u'ぺ').\
                    replace(u'゜ほ', u'ぽ').\
                    replace(u'゜ハ', u'パ').\
                    replace(u'゜ヒ', u'ピ').\
                    replace(u'゜フ', u'プ').\
                    replace(u'゜ヘ', u'ペ').\
                    replace(u'゜ホ', u'ポ')
    if u"゛" in text:
        text = text.replace(u'゛か', u'が').\
                    replace(u'゛き', u'ぎ').\
                    replace(u'゛く', u'ぐ').\
                    replace(u'゛け', u'げ').\
                    replace(u'゛こ', u'ご').\
                    replace(u'゛さ', u'ざ').\
                    replace(u'゛し', u'じ').\
                    replace(u'゛す', u'ず').\
                    replace(u'゛せ', u'ぜ').\
                    replace(u'゛そ', u'ぞ').\
                    replace(u'゛た', u'だ').\
                    replace(u'゛ち', u'ぢ').\
                    replace(u'゛つ', u'づ').\
                    replace(u'゛て', u'で').\
                    replace(u'゛と', u'ど').\
                    replace(u'゛は', u'ば').\
                    replace(u'゛ひ', u'び').\
                    replace(u'゛ふ', u'ぶ').\
                    replace(u'゛へ', u'べ').\
                    replace(u'゛ほ', u'ぼ').\
                    replace(u'゛カ', u'ガ').\
                    replace(u'゛キ', u'ギ').\
                    replace(u'゛ク', u'グ').\
                    replace(u'゛ケ', u'ゲ').\
                    replace(u'゛コ', u'ゴ').\
                    replace(u'゛サ', u'ザ').\
                    replace(u'゛シ', u'ジ').\
                    replace(u'゛ス', u'ズ').\
                    replace(u'゛セ', u'ゼ').\
                    replace(u'゛ソ', u'ゾ').\
                    replace(u'゛タ', u'ダ').\
                    replace(u'゛チ', u'ヂ').\
                    replace(u'゛ツ', u'ヅ').\
                    replace(u'゛テ', u'デ').\
                    replace(u'゛ト', u'ド').\
                    replace(u'゛ハ', u'バ').\
                    replace(u'゛ヒ', u'ビ').\
                    replace(u'゛フ', u'ブ').\
                    replace(u'゛ヘ', u'ベ').\
                    replace(u'゛ホ', u'ボ')
    return text


def print_charmap():
    """Print the symbol table.

    It is much faster to open this file with text editor.
    """

    for i, v in charmap.iteritems():
        print u'%02X:%s' % (i, v)

if __name__ == "__main__":
    print_charmap()
