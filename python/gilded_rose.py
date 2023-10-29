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
        if item.quality > 0:
            item.quality = item.quality - 1
        if item.sell_in < 0:
            item.quality = item.quality - 1
        return item

    def update_sell_in(self, item: Item) -> Item:
        item.sell_in = item.sell_in - 1
        return item


class UpdaterSulfuras:
    def update_quality(self, item: Item) -> Item:
        return item

    def update_sell_in(self, item: Item) -> Item:
        return item


class UpdaterBackstagePass:
    def update_quality(self, item: Item) -> Item:
        if item.sell_in < 6:
            item.quality += 3
        elif item.sell_in < 11:
            item.quality += 2
        else:
            item.quality += 1
        item.quality = min(item.quality, 50)
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = 0
        return item

    def update_sell_in(self, item: Item) -> Item:
        return item


class UpdaterAgedBrie:
    def update_quality(self, item: Item) -> Item:
        if item.quality < 50:
            item.quality = item.quality + 1
        if item.sell_in < 0:
            if item.quality < 50:
                item.quality = item.quality + 1
        item.sell_in = item.sell_in - 1
        return item

    def update_sell_in(self, item: Item) -> Item:
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
