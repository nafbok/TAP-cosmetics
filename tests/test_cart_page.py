import logging
from asyncio import sleep

from selenium.webdriver.common.by import By

from conftest import BaseTest
from constants.base import BaseConstants


class TestCartPage(BaseTest):

    def test_add_item_to_cart(self, driver):
        """Add item to the cart:
            - Load start page;
            - Go to the shop page;
            - Click first product block. Go to the product list page;
            - Click first item. Go to the item page;
            - Press В корзину button;
            - Checked message the item was added to the cart;
            - Click the Просмотр корзины button;
            - Checked the Update cart is enable
            """
        # Load start page
        driver.get(BaseConstants.URL)
        sleep(5)

        # Go to the shop page
        shop_button = driver.find_element(by=By.XPATH, value=".//*[@id='menu-item-118']")
        sleep(3)
        shop_button.click()
        sleep(5)
        self.log.info("Shop page is opened")

        # Click first product block. Go to the product list page;
        product_block = driver.find_element(by=By.XPATH, value='//*[@id="content"]/div[3]/div[1]/div/a[1]/div/img')
        sleep(3)
        product_block.click()
        self.log.info("Product is opened")
