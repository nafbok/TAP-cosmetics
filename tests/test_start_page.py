from time import sleep

from conftest import BaseTest
from constants.base import BaseConstants


class TestStartPage(BaseTest):

    def test_start_page(self, driver):
        """Load start page"""
        driver.get(BaseConstants.URL)
        sleep(5)

