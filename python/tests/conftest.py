import configparser
import os
import pytest


config = configparser.ConfigParser()
config_file = os.path.join(os.path.dirname(__file__), '..', 'settings.ini')
config.read(config_file)
default = config['DEFAULT']

@pytest.fixture
def sulfuras_name():
    return default.get('SULFURAS')


@pytest.fixture
def backstage_pass_name():
    return default.get('BACKSTAGE_PASS')


@pytest.fixture
def aged_brie_name():
    return default.get('AGED_BRIE')
