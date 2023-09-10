import pytest
from gilded_rose import GildedRose, Item


ITEM_NAME = "foo"
MAX_QUALITY = 50
MIN_QUALITY = 0
MAX_SELL_IN = 10
NEGATIVE_SELL_IN = -1


def test_given_a_max_quality_and_large_sell_in_item_when_update_quality_then_it_should_decrease_quality_by_1():
    item = Item(ITEM_NAME, MAX_SELL_IN, MAX_QUALITY)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert gilded_rose.items[0].quality == MAX_QUALITY - 1


def test_given_a_min_quality_item_when_update_quality_then_it_should_keep_the_same_quality_as_before():
    item = Item(ITEM_NAME, MAX_SELL_IN, MIN_QUALITY)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert gilded_rose.items[0].quality == MIN_QUALITY


def test_given_a_negative_sell_in_item_when_update_quality_then_it_should_decrease_quality_by_2():
    item = Item(ITEM_NAME, NEGATIVE_SELL_IN, MAX_QUALITY)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert gilded_rose.items[0].quality == MAX_QUALITY - 2


def test_given_an_item_when_update_quality_then_it_should_decrease_sell_in():
    item = Item(ITEM_NAME, MAX_SELL_IN, MAX_QUALITY)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert gilded_rose.items[0].sell_in == MAX_SELL_IN - 1
