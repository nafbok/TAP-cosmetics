from pages.base_page import BasePage
from pages.header import Header



class StartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.header = Header(self.driver)






