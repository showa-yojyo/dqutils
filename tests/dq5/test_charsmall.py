"""Tests for dqutils.dq5.charsmall module."""

import pytest

from dqutils.dq5.charsmall import process_dakuten


@pytest.mark.parametrize(
    "pair",
    [
        ("゜は", "ぱ"),
        ("゜ひ", "ぴ"),
        ("゜ふ", "ぷ"),
        ("゜へ", "ぺ"),
        ("゜ほ", "ぽ"),
        ("゜ハ", "パ"),
        ("゜ヒ", "ピ"),
        ("゜フ", "プ"),
        ("゜ヘ", "ペ"),
        ("゜ホ", "ポ"),
        ("゛か", "が"),
        ("゛き", "ぎ"),
        ("゛く", "ぐ"),
        ("゛け", "げ"),
        ("゛こ", "ご"),
        ("゛さ", "ざ"),
        ("゛し", "じ"),
        ("゛す", "ず"),
        ("゛せ", "ぜ"),
        ("゛そ", "ぞ"),
        ("゛た", "だ"),
        ("゛ち", "ぢ"),
        ("゛つ", "づ"),
        ("゛て", "で"),
        ("゛と", "ど"),
        ("゛は", "ば"),
        ("゛ひ", "び"),
        ("゛ふ", "ぶ"),
        ("゛へ", "べ"),
        ("゛ほ", "ぼ"),
        ("゛カ", "ガ"),
        ("゛キ", "ギ"),
        ("゛ク", "グ"),
        ("゛ケ", "ゲ"),
        ("゛コ", "ゴ"),
        ("゛サ", "ザ"),
        ("゛シ", "ジ"),
        ("゛ス", "ズ"),
        ("゛セ", "ゼ"),
        ("゛ソ", "ゾ"),
        ("゛タ", "ダ"),
        ("゛チ", "ヂ"),
        ("゛ツ", "ヅ"),
        ("゛テ", "デ"),
        ("゛ト", "ド"),
        ("゛ハ", "バ"),
        ("゛ヒ", "ビ"),
        ("゛フ", "ブ"),
        ("゛ヘ", "ベ"),
        ("゛ホ", "ボ"),
    ],
)
def test_process_replacement(pair):
    """Test function dqutils.dq5.process_dakuten."""
    native, readable = pair
    assert process_dakuten(native) == readable


@pytest.mark.parametrize(
    "fixed",
    [
        "゛",
        "゛゛",
        "゜",
        "゜゜",
    ],
)
def test_process_preseved(fixed):
    """Test function dqutils.dq5.process_dakuten."""
    assert process_dakuten(fixed) == fixed
