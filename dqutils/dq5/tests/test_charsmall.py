# -*- coding: utf-8 -*-
"""Tests for dqutils.dq5.charsmall module."""

from unittest import TestCase
from dqutils.dq5.charsmall import process_dakuten

class DQ5CharSmallTestCase(TestCase):
    """Test functions defined in dqutils.dq5.charsmall."""

    def test_process_replacement(self):
        """Test function dqutils.dq5.process_dakuten."""

        data = (('゜は', 'ぱ'),
                ('゜ひ', 'ぴ'),
                ('゜ふ', 'ぷ'),
                ('゜へ', 'ぺ'),
                ('゜ほ', 'ぽ'),
                ('゜ハ', 'パ'),
                ('゜ヒ', 'ピ'),
                ('゜フ', 'プ'),
                ('゜ヘ', 'ペ'),
                ('゜ホ', 'ポ'),
                ('゛か', 'が'),
                ('゛き', 'ぎ'),
                ('゛く', 'ぐ'),
                ('゛け', 'げ'),
                ('゛こ', 'ご'),
                ('゛さ', 'ざ'),
                ('゛し', 'じ'),
                ('゛す', 'ず'),
                ('゛せ', 'ぜ'),
                ('゛そ', 'ぞ'),
                ('゛た', 'だ'),
                ('゛ち', 'ぢ'),
                ('゛つ', 'づ'),
                ('゛て', 'で'),
                ('゛と', 'ど'),
                ('゛は', 'ば'),
                ('゛ひ', 'び'),
                ('゛ふ', 'ぶ'),
                ('゛へ', 'べ'),
                ('゛ほ', 'ぼ'),
                ('゛カ', 'ガ'),
                ('゛キ', 'ギ'),
                ('゛ク', 'グ'),
                ('゛ケ', 'ゲ'),
                ('゛コ', 'ゴ'),
                ('゛サ', 'ザ'),
                ('゛シ', 'ジ'),
                ('゛ス', 'ズ'),
                ('゛セ', 'ゼ'),
                ('゛ソ', 'ゾ'),
                ('゛タ', 'ダ'),
                ('゛チ', 'ヂ'),
                ('゛ツ', 'ヅ'),
                ('゛テ', 'デ'),
                ('゛ト', 'ド'),
                ('゛ハ', 'バ'),
                ('゛ヒ', 'ビ'),
                ('゛フ', 'ブ'),
                ('゛ヘ', 'ベ'),
                ('゛ホ', 'ボ'),)

        for i, j in data:
            self.assertEqual(process_dakuten(i), j)

    def test_process_preseved(self):
        """Test function dqutils.dq5.process_dakuten."""

        data = ('゛',
                '゛゛',
                '゜',
                '゜゜',)

        for i in data:
            self.assertEqual(process_dakuten(i), i)
