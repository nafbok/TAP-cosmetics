from conftest import BaseTest


class TestStartPage(BaseTest):

    def test_refresh_start_page(self, start_page):
        """Click logo and refresh start page"""
        start_page.header.click_logo()
        self.log.debug("Start page was refreshed")

    def test_search_item_by_value(self, start_page):
        """Search item:
        - Click search icon to open search bar
        - Fill search bar by provided data
        - Click Search button
        - Verify the result of the search is loaded"""

        # Click search icon to open search bar
        start_page.header.open_search_bar()

        # Fill search bar by provided data
        item = self.random_value()
        start_page.header.fill_search_bar(item)

        # Click Search button
        search_result = start_page.header.search_item_by_provided_value()

        # Verify the result of the search is loaded
        search_result.verify_search_result()




