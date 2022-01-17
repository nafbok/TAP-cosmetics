from constants.antisaptic_list_page import AntisepticListConstants
from pages.base_page import BasePage
from pages.item_antiseptic_page import ItemAntisepticPage
from pages.utils import log_decorator


class AntisepticListPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = AntisepticListConstants()

    @log_decorator
    def move_to_item_antiseptic_page(self):
        """Go to the item antiseptic page and return it"""
        item_grid = self.wait_until_find_element(value=self.constants.GRID_ANTISEPTIC_XPATH)
        item_grid.click()
        return ItemAntisepticPage(self.driver)




