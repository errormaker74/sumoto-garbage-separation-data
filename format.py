# -*- coding: utf-8 -*-
import json

from utils import JSON_PATH, read_json


def main() -> None:
    """
    jsonのデータを整形して出力する。
    """
    data = read_json()
    with open(JSON_PATH, mode='w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    main()
