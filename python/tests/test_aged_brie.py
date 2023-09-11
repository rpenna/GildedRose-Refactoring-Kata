import pytest
from gilded_rose import AGED_BRIE, GildedRose, Item


DEFAULT_QUALITY = 10
MAX_QUALITY = 50
DEFAULT_SELL_IN = 10
ZERO_SELL_IN = 0


@pytest.fixture
def aged_brie():
    return Item(AGED_BRIE, DEFAULT_SELL_IN, DEFAULT_QUALITY)


@pytest.fixture
def max_quality_aged_brie():
    return Item(AGED_BRIE, DEFAULT_SELL_IN, MAX_QUALITY)


def test_given_an_aged_brie_item_that_has_not_reached_max_quality_when_update_quality_then_it_should_increase_quality(
    aged_brie,
):
    gilded_rose = GildedRose([aged_brie])
    gilded_rose.update_quality()
    assert gilded_rose.items[0].quality == DEFAULT_QUALITY + 1


def test_given_a_max_quality_aged_brie_item_when_update_quality_then_it_should_keep_the_same_quality(
    max_quality_aged_brie,
):
    gilded_rose = GildedRose([max_quality_aged_brie])
    gilded_rose.update_quality()
    assert gilded_rose.items[0].quality == MAX_QUALITY


def test_given_a_zero_sell_in_aged_brie_when_update_quality_then_it_should_increase_quality_by_1():
    aged_brie = Item(AGED_BRIE, 0, DEFAULT_QUALITY)
    gilded_rose = GildedRose([aged_brie])
    gilded_rose.update_quality()
    assert gilded_rose.items[0].quality == DEFAULT_QUALITY + 1
