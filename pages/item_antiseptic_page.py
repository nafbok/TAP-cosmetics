from constants.item_antiseptic_page import ItemAntisepticConstants
from pages.base_page import BasePage
from pages.cart_page import CartPage
from pages.utils import log_decorator


class ItemAntisepticPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = ItemAntisepticConstants()

    @log_decorator
    def add_item_to_cart(self):
        """Add item to the cart"""
        add_to_cart = self.wait_until_find_element(value=self.constants.ADD_ITEM_TO_CART_BUTTON_XPATH)
        add_to_cart.click()

    @log_decorator
    def verify_message(self):
        """Verify the message od the added item is displayed"""
        message_add_to_cart = self.wait_until_element_enabled(value=self.constants.MESSEGE_ITEM_ADDED_XPATH)
        assert message_add_to_cart.is_displayed()

    @log_decorator
    def verify_show_cart_is_displayed(self):
        """Verify Show cart button is displayed"""
        show_cart = self.wait_until_find_element(value=self.constants.SHOW_CART_BUTTON_XPATH)
        assert show_cart.is_displayed()

    @log_decorator
    def move_to_cart_page(self):
        """Move to the Cart page and return it"""
        cart = self.wait_until_find_element(value=self.constants.SHOW_CART_BUTTON_XPATH)
        cart.click()
        return CartPage(self.driver)

