from constants.cart_page import CartConstants
from pages.base_page import BasePage
from pages.checkout_page import CheckoutPage
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

    @log_decorator
    def remove_item_from_cart(self):
        """Click remove icon and remove the item"""
        remove_item = self.wait_until_find_element(value=self.constants.REMOVE_ICON_XPATH)
        remove_item.click()

    @log_decorator
    def verify_message_empty_cart(self):
        """Verify the message the empty cart is displayed"""
        message_empty_cart = self.wait_until_element_enabled(value=self.constants.REMOVE_ITEM_MESSAGE_XPATH)
        assert message_empty_cart.text == self.constants.REMOVE_TEXT_MESSAGE_XPATH

    @log_decorator
    def proceed_to_checkout_page(self):
        """Move to Checkout page and return it"""
        checkout_button = self.wait_until_find_element(value=self.constants.PROCEED_TO_CHECKOUT_BUTTON_XPATH)
        checkout_button.click()
        return CheckoutPage(self.driver)
