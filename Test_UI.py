import pytest
import pytest_check as check
from selenium import webdriver
from selenium.webdriver.common.by import By
import TakeScreenShot


class TestSearch:

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome()
        self.bookstoreUrl = "https://automationbookstore.dev/"
        self.driver.maximize_window()
        yield
        TakeScreenShot.get_screenshot(self.driver, self.TEST_NAME)
        self.driver.close()
        self.driver.quit()

    @pytest.mark.gui_tests
    def test_01_bookstore_page_title(self, setup):
        """ Test to make sure the current title is displayed. """
        self.TEST_NAME = "Page_title_test"
        self.driver.get(self.bookstoreUrl)
        title = self.bookstoreUrl.title()
        check.is_true(title)

    @pytest.mark.gui_tests
    def test_02_search_pos(self, setup):
        """ Test to make sure that the search finds a book by keyword """
        self.TEST_NAME = "Search_pos_test"
        self.driver.get(self.bookstoreUrl)
        search_bar = self.driver.find_element(By.ID, "searchBar")
        search_bar.send_keys("Google")
        result = self.driver.find_element(By.ID, "pid4")
