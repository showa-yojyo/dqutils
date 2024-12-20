"""dqutils.dq3.charsmall - The dictionary of small size characters."""

# ruff: noqa: RUF001
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Final

CHARMAP: Final[dict[int, str]] = {
    0x00: "",
    0x01: " ",
    0x02: "/",
    0x03: "゜",
    0x04: "゛",
    0x05: "：",
    0x06: "Ex",
    0x07: "Lv",
    0x08: "―",
    0x09: "＊",
    0x0A: "ど",
    0x0B: ".",
    0x0C: "あ",
    0x0D: "い",
    0x0E: "う",
    0x0F: "え",
    0x10: "お",
    0x11: "か",
    0x12: "き",
    0x13: "く",
    0x14: "け",
    0x15: "こ",
    0x16: "さ",
    0x17: "し",
    0x18: "す",
    0x19: "せ",
    0x1A: "そ",
    0x1B: "た",
    0x1C: "ち",
    0x1D: "つ",
    0x1E: "て",
    0x1F: "と",
    0x20: "な",
    0x21: "に",
    0x22: "ぬ",
    0x23: "ね",
    0x24: "の",
    0x25: "は",
    0x26: "ひ",
    0x27: "ふ",
    0x28: "へ",
    0x29: "ほ",
    0x2A: "ま",
    0x2B: "み",
    0x2C: "む",
    0x2D: "め",
    0x2E: "も",
    0x2F: "や",
    0x30: "ゆ",
    0x31: "よ",
    0x32: "ら",
    0x33: "り",
    0x34: "る",
    0x35: "れ",
    0x36: "ろ",
    0x37: "わ",
    0x38: "を",
    0x39: "ん",
    0x3A: "ぁ",
    0x3B: "ぃ",
    0x3C: "ぅ",
    0x3D: "ぇ",
    0x3E: "ぉ",
    0x3F: "っ",
    0x40: "ゃ",
    0x41: "ゅ",
    0x42: "ょ",
    0x43: "ア",
    0x44: "イ",
    0x45: "ウ",
    0x46: "エ",
    0x47: "オ",
    0x48: "カ",
    0x49: "キ",
    0x4A: "ク",
    0x4B: "ケ",
    0x4C: "コ",
    0x4D: "サ",
    0x4E: "シ",
    0x4F: "ス",
    0x50: "セ",
    0x51: "ソ",
    0x52: "タ",
    0x53: "チ",
    0x54: "ツ",
    0x55: "テ",
    0x56: "ト",
    0x57: "ナ",
    0x58: "ニ",
    0x59: "ヌ",
    0x5A: "ネ",
    0x5B: "ノ",
    0x5C: "ハ",
    0x5D: "ヒ",
    0x5E: "フ",
    0x5F: "ヘ",
    0x60: "ホ",
    0x61: "マ",
    0x62: "ミ",
    0x63: "ム",
    0x64: "メ",
    0x65: "モ",
    0x66: "ヤ",
    0x67: "ユ",
    0x68: "ヨ",
    0x69: "ラ",
    0x6A: "リ",
    0x6B: "ル",
    0x6C: "レ",
    0x6D: "ロ",
    0x6E: "ワ",
    0x6F: "ヲ",
    0x70: "ン",
    0x71: "ァ",
    0x72: "ィ",
    0x73: "ゥ",
    0x74: "ェ",
    0x75: "ォ",
    0x76: "ッ",
    0x77: "ャ",
    0x78: "ュ",
    0x79: "ョ",
    0x7A: "E",
    0x7B: " ",
    0x7C: "★",
    0x7D: "ー",
    0x7E: "？",
    0x7F: "！",
    0x80: "▼",
    0x81: "〓",
    0x82: "→",
    0x83: "。",
    0x84: ".",
    0x85: "「",
    0x86: "…",
    0x87: "０",
    0x88: "１",
    0x89: "２",
    0x8A: "３",
    0x8B: "４",
    0x8C: "５",
    0x8D: "６",
    0x8E: "７",
    0x8F: "８",
    0x90: "９",
    0x91: "Ａ",
    0x92: "Ｂ",
    0x93: "Ｃ",
    0x94: "Ｄ",
    0x95: "Ｅ",
    0x96: "Ｆ",
    0x97: "Ｇ",
    0x98: "Ｈ",
    0x99: "Ｉ",
    0x9A: "Ｊ",
    0x9B: "Ｋ",
    0x9C: "Ｌ",
    0x9D: "Ｍ",
    0x9E: "Ｎ",
    0x9F: "Ｏ",
    0xA0: "Ｐ",
    0xA1: "Ｑ",
    0xA2: "Ｒ",
    0xA3: "Ｓ",
    0xA4: "Ｔ",
    0xA5: "Ｕ",
    0xA6: "Ｖ",
    0xA7: "Ｗ",
    0xA8: "Ｘ",
    0xA9: "Ｙ",
    0xAA: "Ｚ",
    # 0xAB:"[AB]",
    # 0xAC:"[AC]",
    # 0xAD:"[AD]",
    # 0xAE:"[AE]",
    # 0xAF:"[AF]",
    # 0xB0:"[B0]",
    # 0xB1:"[B1]",
    # 0xB2:"[B2]",
    # 0xB3:"[B3]",
    # 0xB4:"[B4]",
    # 0xB5:"[B5]",
    # 0xB6:"[B6]",
    # 0xB7:"[B7]",
    # 0xB8:"[B8]",
    # 0xB9:"[B9]",
    # 0xBA:"[BA]",
    # 0xBB:"[BB]",
    # 0xBC:"[BC]",
    # 0xBD:"[BD]",
    # 0xBE:"[BE]",
    # 0xBF:"[BF]",
    # 0xC0:"[C0]",
    # 0xC1:"[C1]",
    # 0xC2:"[C2]",
    # 0xC3:"[C3]",
    # 0xC4:"[C4]",
    # 0xC5:"[C5]",
    # 0xC6:"[C6]",
    # 0xC7:"[C7]",
    # 0xC8:"[C8]",
    0xC9: "が",
    0xCA: "ぎ",
    0xCB: "ぐ",
    0xCC: "げ",
    0xCD: "ご",
    0xCE: "ざ",
    0xCF: "じ",
    0xD0: "ず",
    0xD1: "ぜ",
    0xD2: "ぞ",
    0xD3: "だ",
    0xD4: "ぢ",
    0xD5: "づ",
    0xD6: "で",
    0xD7: "ど",
    0xD8: "ば",
    0xD9: "び",
    0xDA: "ぶ",
    0xDB: "べ",
    0xDC: "ぼ",
    0xDD: "ヴ",
    0xDE: "ガ",
    0xDF: "ギ",
    0xE0: "グ",
    0xE1: "ゲ",
    0xE2: "ゴ",
    0xE3: "ザ",
    0xE4: "ジ",
    0xE5: "ズ",
    0xE6: "ゼ",
    0xE7: "ゾ",
    0xE8: "ダ",
    0xE9: "ヂ",
    0xEA: "ヅ",
    0xEB: "デ",
    0xEC: "ド",
    0xED: "バ",
    0xEE: "ビ",
    0xEF: "ブ",
    0xF0: "べ",
    0xF1: "ボ",
    0xF2: "ぱ",
    0xF3: "ぴ",
    0xF4: "ぷ",
    0xF5: "ぺ",
    0xF6: "ぽ",
    0xF7: "パ",
    0xF8: "ピ",
    0xF9: "プ",
    0xFA: "ペ",
    0xFB: "ポ",
    0xFC: "～",
    0xFD: "＋",
    0xFE: "ぬ",
    0xFF: "Ｊ",
}
