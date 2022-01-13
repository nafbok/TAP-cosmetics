from constants.beard_and_mustache_list_page import BeardMustacheConstants
from pages.base_page import BasePage
from pages.beard_mustache_item_page import BeardMustacheItemPage
from pages.utils import log_decorator


class BeardMustacheListPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = BeardMustacheConstants()

    @log_decorator
    def move_to_item_beard_mustache_page(self):
        """Go to the item Beard and mustache page and return it"""
        beard_item_grid = self.wait_until_find_element(value=self.constants.GRID_FIRST_BEARD_ITEM_XPATH)
        beard_item_grid.click()
        return BeardMustacheItemPage(self.driver)