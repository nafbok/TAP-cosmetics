from constants.shop_page import ShopPageConstants
from pages.antisaptic__list_page import AntisepticListPage
from pages.base_page import BasePage
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


