import pytest
import pytest_check as check
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestSearch:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.bookstoreUrl = "https://automationbookstore.dev/"
        self.driver.maximize_window()
        yield
        self.driver.close()
        self.driver.quit()

    def bookstore_page_title(self, setup):
        """ Test to make sure the current title is displayed. """
        self.driver.get(self.bookstoreUrl)
        title = self.bookstoreUrl.title()
        check.is_true(title)

    def search_pos(self, setup):
        """ Test to make sure that the search finds a book by keyword """
        self.driver.get(self.bookstoreUrl)
        search_bar = self.driver.find_element(By.ID, "searchBar")
        search_bar.send_keys("Google")
        result = self.driver.find_element(By.ID, "pid4")
        print (result)


def main(self):

    t1 = TestSearch()
    t1.bookstore_page_title()
    t1.search_pos()
    # pass


if __name__ == "__main__":
    main()