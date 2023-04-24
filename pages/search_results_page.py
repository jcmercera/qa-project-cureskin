from selenium.webdriver.common.by import By
from selenium import webdriver
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC
from sample_script import driver


# from selenium import EC

class SearchResults(Page):
    SEARCH_RESULTS = (By.ID, 'predictive-search-results-list')
    FIRST_PRODUCT = (By.CSS_SELECTOR, 'a.card-information__text.h4')
    SEARCH_DROPDOWN = (By.CSS_SELECTOR, 'ul.search__recommendation.list-unstyled')
    DUMMY_RESULTS_PAGE = (By.CSS_SELECTOR, 'h2.title.title--primary')
    DUMMY_RESULTS_DROPDOWN = (By.CSS_SELECTOR, "div.predictive-search-results")

    def verify_sun_protection_shown(self, expected_result):
        actual_result = self.driver.current_url
        assert expected_result in actual_result, f'Expected {expected_result}, but got {actual_result}'

    def verify_first_product(self, expected_result):
        actual_result = self.driver.find_element(*self.FIRST_PRODUCT).text
        assert expected_result in actual_result, f'Expected {expected_result}, but got {actual_result}'

    def verify_no_results_page(self, *locator):
        expected_result = 'No results'
        actual_result = self.driver.find_element(*self.DUMMY_RESULTS_PAGE).text
        assert expected_result in actual_result, f'Expected {expected_result}, but got {actual_result}'

    def verify_no_results_found(self):
        expected_result = self.driver.find_element(*self.SEARCH_RESULTS)
        actual_result = self.driver.find_element(*self.DUMMY_RESULTS_DROPDOWN)
        assert expected_result is not actual_result
