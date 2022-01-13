import pytest

from conftest import BaseTest


class TestCartPage(BaseTest):


    def test_add_item_to_cart_without_login(self, start_page):
        """ PreConditions:
                - Load the start page
            Add item to the cart without login:
                - Go to the shop page;
                - Click first product block. Go to the antiseptic list page;
                - Click first antiseptic item. Go to the antiseptic item page;
                - Press "В корзину" button;
                - Checked message the item was added to the cart;
                - Checked the "Просмотр корзины" is displayed;
                - Click the Просмотр корзины button;
                - Checked the Update cart is enable
            """
        # Go to the shop page
        shop = start_page.header.move_to_shop()

        # Click first product block. Go to the antiseptic list page
        antiseptic_category = shop.move_to_antiseptic_category()

        # Click first antiseptic item. Go to the antiseptic item page
        antiseptic_item = antiseptic_category.move_to_item_antiseptic_page()

        # Press "В корзину" button
        antiseptic_item.add_item_to_cart()

        # Checked message the item was added to the cart
        antiseptic_item.verify_message()

        # Checked the "Просмотр корзины" is displayed
        antiseptic_item.verify_show_cart_is_displayed()

        # Click the Просмотр корзины button
        cart_page = antiseptic_item.move_to_cart_page()

        # Checked the Update cart is enable
        cart_page.verify_update_cart_is_displayed()

    def test_add_several_item_to_cart_without_login(self, start_page):
        """ PreConditions:
                - Load the start page
            Add several items to the cart without login:
                - Go to the shop page;
                - Click first product block. Go to the antiseptic list page;
                - Click first antiseptic item. Go to the antiseptic item page;
                - Press "В корзину" button;
                - Return to the Shop;
                - Click Beard and mustache product block. Go to the antiseptic list page;
                - Click first item from Beard and mustache block. Go to the item page;
                - Press "В корзину" button;
                - Checked the "Просмотр корзины" is displayed;
                - Click the Просмотр корзины button;
                - Checked the Update cart is enable;
            """
        # Go to the shop page
        shop = start_page.header.move_to_shop()

        # Click first product block. Go to the antiseptic list page
        antiseptic_category = shop.move_to_antiseptic_category()

        # Click first antiseptic item. Go to the antiseptic item page
        antiseptic_item = antiseptic_category.move_to_item_antiseptic_page()

        # Press "В корзину" button
        antiseptic_item.add_item_to_cart()

        # Return to the Shop
        shop = antiseptic_item.header.move_to_shop()

        # Click Beard and mustache product block. Go to the antiseptic list page
        beard_mustache_category = shop.move_to_beard_mustache_category()

        # Click first item from Beard and mustache block. Go to the item page
        beard_item_page = beard_mustache_category.move_to_item_beard_mustache_page()

        # Press "В корзину" button;
        beard_item_page.add_beard_item_to_cart()

        # Checked the "Просмотр корзины" is displayed
        beard_item_page.verify_show_cart_is_displayed()

        # Click the Просмотр корзины button
        cart_page = beard_item_page.move_to_cart_page()

        # Checked the Update cart is enable
        cart_page.verify_update_cart_is_displayed()





















