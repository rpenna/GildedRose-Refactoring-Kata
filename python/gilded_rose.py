# -*- coding: utf-8 -*-
###############################
#           ToDos
# 1. Add new item "Conjured"
# 2. Update README.md
# 3. Create config file to store constants
#
###############################


from typing import Protocol


AGED_BRIE = "Aged Brie"
BACKSTAGE_PASS = "Backstage passes to a TAFKAL80ETC concert"
SULFURAS = "Sulfuras, Hand of Ragnaros"


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


class UpdaterSulfuras:
    def update_quality(self, item: Item) -> Item:
        return item


class UpdaterBackstagePass:
    def update_quality(self, item: Item) -> Item:
        if item.quality < 50:
            item.quality = item.quality + 1
            if item.sell_in < 11:
                if item.quality < 50:
                    item.quality = item.quality + 1
            if item.sell_in < 6:
                if item.quality < 50:
                    item.quality = item.quality + 1
        item.sell_in = item.sell_in - 1
        if item.sell_in < 0:
            item.quality = 0
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


class UpdaterDefaultItem:
    def update_quality(self, item: Item) -> Item:
        if item.quality > 0:
            item.quality = item.quality - 1
        item.sell_in = item.sell_in - 1
        if item.sell_in >= 0:
            return
        if item.quality > 0:
            item.quality = item.quality - 1
        return item


class GildedRose(object):
    def __init__(self, items):
        self.items = items
        self.__items_updaters = dict()
        self.__items_updaters[SULFURAS] = UpdaterSulfuras
        self.__items_updaters[AGED_BRIE] = UpdaterAgedBrie
        self.__items_updaters[BACKSTAGE_PASS] = UpdaterBackstagePass

    def update_quality(self):
        for item in self.items:
            updater = self.__items_updaters.get(item.name, UpdaterDefaultItem)()
            item = updater.update_quality(item)
