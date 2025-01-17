import pytest
from gilded_rose import GildedRose, Item


LONG_TERM_SELL_IN = 15
MEDIUM_TERM_SELL_IN = 10
SHORT_TERM_SELL_IN = 5
EXPIRED_SELL_IN = -1
INITIAL_QUALITY = 0
MAX_QUALITY = 50
DEFAULT_QUALITY = 25


def test_given_a_long_term_sell_in_backstage_pass_when_update_quality_then_it_should_increase_quality_by_1(backstage_pass_name):
    backstage_pass = Item(backstage_pass_name, LONG_TERM_SELL_IN, DEFAULT_QUALITY)
    gilded_rose = GildedRose([backstage_pass])
    gilded_rose.update_quality()
    assert gilded_rose.items[0].quality == DEFAULT_QUALITY + 1


def test_given_a_long_term_sell_in_backstage_pass_when_update_quality_then_it_should_decresase_sell_in_by_1(backstage_pass_name):
    backstage_pass = Item(backstage_pass_name, LONG_TERM_SELL_IN, DEFAULT_QUALITY)
    gilded_rose = GildedRose([backstage_pass])
    gilded_rose.update_quality()
    assert gilded_rose.items[0].sell_in == LONG_TERM_SELL_IN - 1


def test_given_a_long_term_sell_in_with_max_quality_backstage_pass_when_update_quality_then_quality_should_not_change(backstage_pass_name):
    backstage_pass = Item(backstage_pass_name, LONG_TERM_SELL_IN, MAX_QUALITY)
    gilded_rose = GildedRose([backstage_pass])
    gilded_rose.update_quality()
    assert gilded_rose.items[0].quality == MAX_QUALITY


def test_given_a_medium_term_sell_in_backstage_pass_when_update_quality_then_it_should_decresase_sell_in_by_1(backstage_pass_name):
    backstage_pass = Item(backstage_pass_name, MEDIUM_TERM_SELL_IN, DEFAULT_QUALITY)
    gilded_rose = GildedRose([backstage_pass])
    gilded_rose.update_quality()
    assert gilded_rose.items[0].sell_in == MEDIUM_TERM_SELL_IN - 1


def test_given_a_medium_term_sell_in_backstage_pass_when_update_quality_then_it_should_increase_quality_by_2(backstage_pass_name):
    backstage_pass = Item(backstage_pass_name, MEDIUM_TERM_SELL_IN, DEFAULT_QUALITY)
    gilded_rose = GildedRose([backstage_pass])
    gilded_rose.update_quality()
    assert gilded_rose.items[0].quality == DEFAULT_QUALITY + 2


def test_given_a_medium_term_sell_in_with_max_quality_backstage_pass_when_update_quality_then_quality_should_not_change(backstage_pass_name):
    backstage_pass = Item(backstage_pass_name, MEDIUM_TERM_SELL_IN, MAX_QUALITY)
    gilded_rose = GildedRose([backstage_pass])
    gilded_rose.update_quality()
    assert gilded_rose.items[0].quality == MAX_QUALITY


def test_given_a_short_term_sell_in_backstage_pass_when_update_quality_then_it_should_increase_quality_by_3(backstage_pass_name):
    backstage_pass = Item(backstage_pass_name, SHORT_TERM_SELL_IN, DEFAULT_QUALITY)
    gilded_rose = GildedRose([backstage_pass])
    gilded_rose.update_quality()
    assert gilded_rose.items[0].quality == DEFAULT_QUALITY + 3


def test_given_a_short_term_sell_in_backstage_pass_when_update_quality_then_it_should_decresase_sell_in_by_1(backstage_pass_name):
    backstage_pass = Item(backstage_pass_name, SHORT_TERM_SELL_IN, DEFAULT_QUALITY)
    gilded_rose = GildedRose([backstage_pass])
    gilded_rose.update_quality()
    assert gilded_rose.items[0].sell_in == SHORT_TERM_SELL_IN - 1


def test_given_a_short_term_sell_in_with_max_quality_backstage_pass_when_update_quality_then_quality_should_not_change(backstage_pass_name):
    backstage_pass = Item(backstage_pass_name, SHORT_TERM_SELL_IN, MAX_QUALITY)
    gilded_rose = GildedRose([backstage_pass])
    gilded_rose.update_quality()
    assert gilded_rose.items[0].quality == MAX_QUALITY


def test_given_an_expired_backstage_pass_when_update_quality_then_it_should_decresase_sell_in_by_1(backstage_pass_name):
    backstage_pass = Item(backstage_pass_name, EXPIRED_SELL_IN, DEFAULT_QUALITY)
    gilded_rose = GildedRose([backstage_pass])
    gilded_rose.update_quality()
    assert gilded_rose.items[0].sell_in == EXPIRED_SELL_IN - 1


def test_given_an_expired_backstage_pass_when_update_quality_then_quality_should_be_zero(backstage_pass_name):
    backstage_pass = Item(backstage_pass_name, EXPIRED_SELL_IN, DEFAULT_QUALITY)
    gilded_rose = GildedRose([backstage_pass])
    gilded_rose.update_quality()
    assert gilded_rose.items[0].quality == 0


def test_given_an_expired_sell_in_with_max_quality_backstage_pass_when_update_quality_then_quality_should_be_zero(backstage_pass_name):
    backstage_pass = Item(backstage_pass_name, EXPIRED_SELL_IN, MAX_QUALITY)
    gilded_rose = GildedRose([backstage_pass])
    gilded_rose.update_quality()
    assert gilded_rose.items[0].quality == 0
