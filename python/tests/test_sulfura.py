import pytest
from gilded_rose import Item, GildedRose, SULFURAS


DEFAULT_SELL_IN = 10
DEFAULT_QUALITY = 50

@pytest.fixture
def sulfura():
    return Item(SULFURAS, DEFAULT_SELL_IN, DEFAULT_QUALITY)


def test_given_a_sulfura_item_when_update_quality_then_it_should_keep_the_same_quality_as_before(sulfura):
    gilded_rose = GildedRose([sulfura])
    gilded_rose.update_quality()
    assert gilded_rose.items[0].quality == DEFAULT_QUALITY


def test_given_a_sulfura_item_when_update_quality_then_the_sell_in_should_keep_the_same(sulfura):
    gilded_rose = GildedRose([sulfura])
    gilded_rose.update_quality()
    assert gilded_rose.items[0].sell_in == DEFAULT_SELL_IN