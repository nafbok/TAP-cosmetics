from conftest import BaseTest


class TestStartPage(BaseTest):

    def test_refresh_start_page(self, start_page):
        """Click logo and refresh start page"""
        start_page.click_logo()
        self.log.debug("Start page was refreshed")



