from constants.header import HeaderConstants
from pages.base_page import BasePage
from pages.shop_page import ShopPage
from pages.utils import log_decorator


class Header(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = HeaderConstants()

    @log_decorator
    def move_to_shop(self):
        """Move to Shop page and return it"""
        shop_button = self.wait_until_find_element(value=self.constants.SHOP_XPATH)
        shop_button.click()
        return ShopPage(self.driver)