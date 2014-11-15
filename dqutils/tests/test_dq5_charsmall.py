#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for dqutils.dq5.charsmall module."""

import unittest
from dqutils.dq5.charsmall import process_dakuten

# pylint: disable=too-many-public-methods
class DQ5CharSmallTestCase(unittest.TestCase):
    """Test functions defined in dqutils.dq5.charsmall."""

    def test_process_dakuten_replacement(self):
        """Test function dqutils.dq5.process_dakuten."""

        self.assertEqual(process_dakuten('゜は'), 'ぱ')
        self.assertEqual(process_dakuten('゜ひ'), 'ぴ')
        self.assertEqual(process_dakuten('゜ふ'), 'ぷ')
        self.assertEqual(process_dakuten('゜へ'), 'ぺ')
        self.assertEqual(process_dakuten('゜ほ'), 'ぽ')
        self.assertEqual(process_dakuten('゜ハ'), 'パ')
        self.assertEqual(process_dakuten('゜ヒ'), 'ピ')
        self.assertEqual(process_dakuten('゜フ'), 'プ')
        self.assertEqual(process_dakuten('゜ヘ'), 'ペ')
        self.assertEqual(process_dakuten('゜ホ'), 'ポ')
        self.assertEqual(process_dakuten('゛か'), 'が')
        self.assertEqual(process_dakuten('゛き'), 'ぎ')
        self.assertEqual(process_dakuten('゛く'), 'ぐ')
        self.assertEqual(process_dakuten('゛け'), 'げ')
        self.assertEqual(process_dakuten('゛こ'), 'ご')
        self.assertEqual(process_dakuten('゛さ'), 'ざ')
        self.assertEqual(process_dakuten('゛し'), 'じ')
        self.assertEqual(process_dakuten('゛す'), 'ず')
        self.assertEqual(process_dakuten('゛せ'), 'ぜ')
        self.assertEqual(process_dakuten('゛そ'), 'ぞ')
        self.assertEqual(process_dakuten('゛た'), 'だ')
        self.assertEqual(process_dakuten('゛ち'), 'ぢ')
        self.assertEqual(process_dakuten('゛つ'), 'づ')
        self.assertEqual(process_dakuten('゛て'), 'で')
        self.assertEqual(process_dakuten('゛と'), 'ど')
        self.assertEqual(process_dakuten('゛は'), 'ば')
        self.assertEqual(process_dakuten('゛ひ'), 'び')
        self.assertEqual(process_dakuten('゛ふ'), 'ぶ')
        self.assertEqual(process_dakuten('゛へ'), 'べ')
        self.assertEqual(process_dakuten('゛ほ'), 'ぼ')
        self.assertEqual(process_dakuten('゛カ'), 'ガ')
        self.assertEqual(process_dakuten('゛キ'), 'ギ')
        self.assertEqual(process_dakuten('゛ク'), 'グ')
        self.assertEqual(process_dakuten('゛ケ'), 'ゲ')
        self.assertEqual(process_dakuten('゛コ'), 'ゴ')
        self.assertEqual(process_dakuten('゛サ'), 'ザ')
        self.assertEqual(process_dakuten('゛シ'), 'ジ')
        self.assertEqual(process_dakuten('゛ス'), 'ズ')
        self.assertEqual(process_dakuten('゛セ'), 'ゼ')
        self.assertEqual(process_dakuten('゛ソ'), 'ゾ')
        self.assertEqual(process_dakuten('゛タ'), 'ダ')
        self.assertEqual(process_dakuten('゛チ'), 'ヂ')
        self.assertEqual(process_dakuten('゛ツ'), 'ヅ')
        self.assertEqual(process_dakuten('゛テ'), 'デ')
        self.assertEqual(process_dakuten('゛ト'), 'ド')
        self.assertEqual(process_dakuten('゛ハ'), 'バ')
        self.assertEqual(process_dakuten('゛ヒ'), 'ビ')
        self.assertEqual(process_dakuten('゛フ'), 'ブ')
        self.assertEqual(process_dakuten('゛ヘ'), 'ベ')
        self.assertEqual(process_dakuten('゛ホ'), 'ボ')

    def test_process_dakuten_preseved(self):
        """Test function dqutils.dq5.process_dakuten."""

        self.assertEqual(process_dakuten('゛'), '゛')
        self.assertEqual(process_dakuten('゛゛'), '゛゛')
        self.assertEqual(process_dakuten('゜'), '゜')
        self.assertEqual(process_dakuten('゜゜'), '゜゜')
