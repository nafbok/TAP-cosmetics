from selenium.webdriver.common.by import By

from constants.start_page import StartPageConstants
from pages.base_page import BasePage
from pages.header import Header
from pages.utils import log_decorator


class StartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = StartPageConstants()
        self.header = Header(self.driver)

    @log_decorator
    def click_logo(self):
        """Refresh start page"""
        logo = self.wait_until_find_element(value=self.constants.LOGO_LINK_XPATH)
        logo.click()



