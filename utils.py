# -*- coding: utf-8 -*-
import json
from typing import List, Dict

JSON_PATH = 'data/sumoto-garbage-separation.json'


def read_json() -> List[Dict]:
    """
    sumoto-gomi.jsonの内容を取得する。
    """
    with open(JSON_PATH, mode='r', encoding='utf-8') as f:
        data: List[Dict] = json.load(f)
    return data
