from constants.cart_page import CartConstants
from pages.base_page import BasePage
from pages.utils import log_decorator


class CartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = CartConstants()

    @log_decorator
    def verify_update_cart_is_displayed(self):
        """Verify the updated cart button is displayed"""
        update_cart_button = self.wait_until_find_element(value=self.constants.UPDATE_CART_BUTTON_XPATH)
        assert update_cart_button.is_displayed()