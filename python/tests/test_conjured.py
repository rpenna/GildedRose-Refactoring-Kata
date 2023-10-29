from gilded_rose import GildedRose, Item

ITEM_NAME = "Conjured"
MAX_QUALITY = 50
MIN_QUALITY = 0
DEFAULT_SELL_IN = 10


def test_given_a_non_min_quality_conjured_item_when_update_sell_in_then_it_should_decrease_quality_by_2():
    item = Item(ITEM_NAME, DEFAULT_SELL_IN, MAX_QUALITY)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert gilded_rose.items[0].quality == MAX_QUALITY - 2


def test_given_a_min_quality_conjured_item_when_update_sell_in_then_quality_should_be_equal_to_min_quality():
    item = Item(ITEM_NAME, DEFAULT_SELL_IN, MIN_QUALITY)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert gilded_rose.items[0].quality == MIN_QUALITY


def test_given_a_quality_1_conjured_item_when_update_sell_in_then_quality_should_be_equal_to_min_quality():
    item = Item(ITEM_NAME, DEFAULT_SELL_IN, 1)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert gilded_rose.items[0].quality == MIN_QUALITY
