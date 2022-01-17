from constants.checkout_page import CheckoutConstants
from pages.base_page import BasePage
from pages.utils import log_decorator


class CheckoutPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = CheckoutConstants()

    @log_decorator
    def confirm_order_with_empty_fields(self):
        """Click confirm order button with empty fields"""
        confirm_order_button = self.wait_until_find_element(value=self.constants.CONFIRM_ORDER_BUTTON_XPATH)
        confirm_order_button.click()

    @log_decorator
    def verify_error_name_message(self):
        """Verify Name field should be field"""
        error_message = self.wait_until_find_element(value=self.constants.NAME_MESSAGE_XPATH)
        assert error_message.is_displayed()

    @log_decorator
    def verify_confirm_button_enabled(self):
        """Verify Confirm button is enabled"""
        confirm_button = self.wait_until_element_enabled(value=self.constants.CONFIRM_ORDER_BUTTON_XPATH)
        assert confirm_button.is_displayed()


