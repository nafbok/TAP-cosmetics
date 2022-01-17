from time import sleep

from conftest import BaseTest


class TestCheckoutPage(BaseTest):

    def test_checkout_with_empty_fields(self, start_page):
        """ PreConditions:
                - Load the start page
            Add item to the cart without login:
                - Go to the shop page;
                - Click first product block. Go to the antiseptic list page;
                - Click first antiseptic item. Go to the antiseptic item page;
                - Press "В корзину" button;
                - Checked the "Просмотр корзины" is displayed;
                - Click the Просмотр корзины button;
                - Click Proceed to Checkout;
                - Click Confirm order button;
                - Verify error message is displayed
        """
        # Go to the shop page
        shop = start_page.header.move_to_shop()

        # Click first product block. Go to the antiseptic list page
        antiseptic_category = shop.move_to_antiseptic_category()

        # Click first antiseptic item. Go to the antiseptic item page
        antiseptic_item = antiseptic_category.move_to_item_antiseptic_page()

        # Press "В корзину" button
        antiseptic_item.add_item_to_cart()

        # Checked the "Просмотр корзины" is displayed
        antiseptic_item.verify_show_cart_is_displayed()

        # Click the Просмотр корзины button
        cart_page = antiseptic_item.move_to_cart_page()

        # Click Proceed to Checkout
        confirm_button = cart_page.proceed_to_checkout_page()

        # Check the confirm button is enabled
        confirm_button.verify_confirm_button_enabled()

        # Click Confirm order button
        sleep(3)
        confirm_button.confirm_order_with_empty_fields()

        # Verify error message is displayed
        confirm_button.verify_error_name_message()

