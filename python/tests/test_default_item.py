import pytest
from gilded_rose import GildedRose, Item


ITEM_NAME = 'foo'
MAX_QUALITY = 50
MIN_QUALITY = 0


def test_given_a_max_quality_and_large_sell_in_item_when_update_quality_then_it_should_decrease_quality_by_1():
    item = Item(ITEM_NAME, 100, MAX_QUALITY)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert gilded_rose.items[0].quality == 49
