from __future__ import annotations

import os

import jsonpickle
from typing import List


class Items:
    ITEMS: List[Items] = []
    ITEMS_FILE: str = "items.json"

    def __init__(self, title: str, item_type: int, date_added: str, date_manufactured: str, desc: str):
        self.title = title
        self.type = item_type
        self.date_added = date_added
        self.date_manufactured = date_manufactured
        self.description = desc
        Items.ITEMS.append(self)

    @staticmethod
    def save_to_file() -> None:
        json_object = jsonpickle.encode(Items.ITEMS, unpicklable=False)
        with open(Items.ITEMS_FILE, 'w') as outfile:
            outfile.write(json_object)

    @staticmethod
    def load_from_file() -> None:
        Items.ITEMS.clear()
        if not os.path.isfile(Items.ITEMS_FILE) or not os.path.getsize(Items.ITEMS_FILE) > 0:
            return

        with open(Items.ITEMS_FILE) as infile:
            json_object = infile.read()
            item_list = jsonpickle.decode(json_object)
            for i in item_list:
                Items(i['title'], i['type'], i['date_added'], i['date_manufactured'], i['description'])
