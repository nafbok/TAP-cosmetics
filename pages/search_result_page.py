from constants.search_result_page import SearchResultConstants
from pages.base_page import BasePage
from pages.utils import log_decorator


class SearchResultPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = SearchResultConstants()

    @log_decorator
    def verify_search_result(self):
        """Verify the search result is loaded"""
        search_result = self.wait_until_find_element(value=self.constants.SEARCH_RESULT_XPATH)
        search_result.is_displayed()
