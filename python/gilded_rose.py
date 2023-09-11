# -*- coding: utf-8 -*-

AGED_BRIE = "Aged Brie"
BACKSTAGE_PASS = "Backstage passes to a TAFKAL80ETC concert"
SULFURAS = "Sulfuras, Hand of Ragnaros"


class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def __update_sulfuras(self):
        return

    def __update_backstage_pass(self, item):
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

    def __update_aged_brie(self, item):
        if item.quality < 50:
            item.quality = item.quality + 1
        if item.sell_in < 0:
            if item.quality < 50:
                item.quality = item.quality + 1
        item.sell_in = item.sell_in - 1

    def __update_default(self, item):
        if item.quality > 0:
            item.quality = item.quality - 1
        item.sell_in = item.sell_in - 1
        if item.sell_in >= 0:
            return
        else:
            if item.quality > 0:
                item.quality = item.quality - 1

    def update_quality(self):
        for item in self.items:
            if item.name == SULFURAS:
                self.__update_sulfuras()
                continue
            if item.name == AGED_BRIE:
                self.__update_aged_brie(item)
                continue
            elif item.name == BACKSTAGE_PASS:
                self.__update_backstage_pass(item)
                continue
            self.__update_default(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return f"{self.name}, {self.sell_in}, {self.quality}"
