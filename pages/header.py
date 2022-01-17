from constants.header import HeaderConstants
from pages.base_page import BasePage
from pages.search_result_page import SearchResultPage
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

    @log_decorator
    def open_search_bar(self):
        """Open search bar"""
        search_icon = self.wait_until_find_element(value=self.constants.SEARCH_ICON_XPATH)
        search_icon.click()

    @log_decorator
    def fill_search_bar(self, value):
        """Fill the search bar"""
        request = self.wait_until_find_element(value=self.constants.SEARCH_BAR_XPATH)
        request.clear()
        request.send_keys(value)

    @log_decorator
    def search_item_by_provided_value(self):
        """Click Search button to find the item"""
        search_button = self.wait_until_find_element(value=self.constants.SEARCH_BUTTON_XPATH)
        search_button.click()
        return SearchResultPage(self.driver)

    @log_decorator
    def click_logo(self):
        """Refresh start page"""
        logo = self.wait_until_find_element(value=self.constants.LOGO_LINK_XPATH)
        logo.click()