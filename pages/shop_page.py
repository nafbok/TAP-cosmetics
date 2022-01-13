from constants.shop_page import ShopPageConstants
from pages.antisaptic__list_page import AntisepticListPage
from pages.base_page import BasePage
from pages.beard_mustache_list_page import BeardMustacheListPage
from pages.utils import log_decorator


class ShopPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = ShopPageConstants()

    @log_decorator
    def move_to_antiseptic_category(self):
        """Click to the Antiseptic category and move there"""
        antiseptic_category = self.wait_until_element_enabled(value=self.constants.ANTISEPTIC_CATEGORY_XPATH)
        antiseptic_category.click()
        return AntisepticListPage(self.driver)

    @log_decorator
    def move_to_beard_mustache_category(self):
        """Click to the Beard and mustache category and move there"""
        beard_mustache_category = self.wait_until_element_enabled(value=self.constants.BEARD_AND_MUSTACHE_XPATH)
        beard_mustache_category.click()
        return BeardMustacheListPage(self.driver)


