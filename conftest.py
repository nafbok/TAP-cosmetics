"""Conftest"""
import logging
import random

import pytest
from selenium.webdriver.chrome import webdriver

from constants.base import BaseConstants
from pages.start_page import StartPage


def pytest_runtest_setup(item):
    item.cls.log = logging.getLogger(item.name)

class BaseTest:
    """Set some fields to provide autocomplete for dynamically added fields"""
    log = logging.getLogger(__name__)

    @pytest.fixture(scope='function')
    def driver(self):
        driver = webdriver.WebDriver(BaseConstants.CHROME_DRIVER)
        driver.maximize_window()
        yield driver
        driver.close()

    @pytest.fixture(scope='function')
    def start_page(self, driver):
        """Return Start page object"""
        driver.get(BaseConstants.URL)
        return StartPage(driver)

    def random_value(self):
        """Choose one item from list"""
        items_list = ['', 'Атисептик', 'Масло', 'Шампунь']
        random.shuffle(items_list)
        value = items_list[0]
        return value