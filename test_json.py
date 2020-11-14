# -*- coding: utf-8 -*-
import json
from typing import List, Dict

from utils import read_json


def test_is_json() -> None:
    """
    jsonデータであるかどうか判定する。
    """
    is_json: bool = True
    try:
        _ = read_json()
    except json.decoder.JSONDecodeError:
        is_json = False
    assert is_json


def test_has_all_keys() -> None:
    """
    jsonのkey項目がすべてそろっているかどうか判定する。
    """
    keys: List[str] = ['item', 'material', 'kind', 'note']

    data: List[Dict] = read_json()
    for d in data:
        for key in keys:
            assert key in d.keys()


def test_has_correct_kind() -> None:
    """
    jsonのごみの種類が規定のものであるか判定する。
    """

    kinds: List[str] = [
        "✖",
        "アルミ缶",
        "スチール缶",
        "びん",
        "プラスチックトレイ",
        "ペットボトル",
        "古着類",
        "雑誌・その他の紙",
        "紙パック",
        "小型家電",
        "新聞",
        "大型ごみ",
        "段ボール",
        "燃えないごみ",
        "燃えるごみ",
        "廃食用油",
        "有害危険ごみ",
    ]

    data: List[Dict] = read_json()

    for d in data:
        assert d['kind'] in kinds
