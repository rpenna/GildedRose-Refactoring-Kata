##################################################
#           ToDos
# 1. Add new item "Conjured"
# 2. Update README.md
# 3. Make "update_quality" methods more readable
#
##################################################

import configparser
import os
from typing import Protocol


config = configparser.ConfigParser()
config_file = os.path.join(os.path.dirname(__file__), "settings.ini")
config.read(config_file)
default_config = config["DEFAULT"]
MIN_QUALITY = int(default_config["MIN_QUALITY"])
MAX_QUALITY = int(default_config["MAX_QUALITY"])


def decrease_item_quality(quality: int, amount: int = 1) -> int:
    return max(MIN_QUALITY, quality - amount)


def increase_item_quality(quality: int, amount: int = 1) -> int:
    return min(MAX_QUALITY, quality + amount)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return f"{self.name}, {self.sell_in}, {self.quality}"


class Updater(Protocol):
    def update_quality(self, item: Item) -> Item:
        pass

    def update_sell_in(self, item: Item) -> Item:
        pass


class UpdaterDefaultItem:
    def update_quality(self, item: Item) -> Item:
        item.quality = decrease_item_quality(item.quality)
        if item.sell_in < 0:
            item.quality = decrease_item_quality(item.quality)
        return item

    def update_sell_in(self, item: Item) -> Item:
        item.sell_in -= 1
        return item


class UpdaterSulfuras(UpdaterDefaultItem):
    def update_quality(self, item: Item) -> Item:
        return item

    def update_sell_in(self, item: Item) -> Item:
        return item


class UpdaterBackstagePass(UpdaterDefaultItem):
    def update_quality(self, item: Item) -> Item:
        if item.sell_in < 0:
            item.quality = 0
            return item
        item.quality = increase_item_quality(item.quality)
        if item.sell_in < 11:
            item.quality = increase_item_quality(item.quality)
        if item.sell_in < 6:
            item.quality = increase_item_quality(item.quality)
        return item

    def update_sell_in(self, item: Item) -> Item:
        item.sell_in -= 1
        return item


class UpdaterAgedBrie(UpdaterDefaultItem):
    def update_quality(self, item: Item) -> Item:
        item.quality = increase_item_quality(item.quality)
        return item

    def update_sell_in(self, item: Item) -> Item:
        item.sell_in = item.sell_in - 1
        return item


class GildedRose(object):
    def __init__(self, items):
        self.items = items
        self.__items_updaters = dict()
        self.__items_updaters[default_config.get("SULFURAS")] = UpdaterSulfuras
        self.__items_updaters[default_config.get("AGED_BRIE")] = UpdaterAgedBrie
        self.__items_updaters[
            default_config.get("BACKSTAGE_PASS")
        ] = UpdaterBackstagePass

    def update_quality(self):
        for item in self.items:
            updater = self.__items_updaters.get(item.name, UpdaterDefaultItem)()
            item = updater.update_sell_in(item)
            item = updater.update_quality(item)
