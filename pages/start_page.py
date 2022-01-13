from pages.base_page import BasePage


class StartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def load_start_page(self):
        """Load start page"""
        return StartPage

