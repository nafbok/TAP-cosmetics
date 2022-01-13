"""Conftest"""
import logging

import pytest
from selenium.webdriver.chrome import webdriver

from constants.base import BaseConstants


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