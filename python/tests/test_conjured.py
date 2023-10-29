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
