from constants.beard_item_mustache_page import BeardMustacheItemConstants
from pages.base_page import BasePage
from pages.cart_page import CartPage
from pages.utils import log_decorator


class BeardMustacheItemPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = BeardMustacheItemConstants()

    @log_decorator
    def add_beard_item_to_cart(self):
        """Add beard item to the cart"""
        add_beard_item_to_cart = self.wait_until_find_element(value=self.constants.ADD_ITEM_TO_CART_BUTTON_XPATH)
        add_beard_item_to_cart.click()

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