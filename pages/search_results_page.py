from selenium.webdriver.common.by import By
from selenium import webdriver
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC
from sample_script import driver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


class SearchResults(Page):
    SEARCH_RESULTS = (By.ID, 'predictive-search-results-list')
    ADD_1ST_TO_CART = (By.CSS_SELECTOR, 'add-to-cart[data-variant-id="32367833382996"]')
    FIRST_PRODUCT = (By.CSS_SELECTOR, 'a.card-information__text.h4')
    SEARCH_DROPDOWN = (By.CSS_SELECTOR, 'ul.search__recommendation.list-unstyled')
    DUMMY_RESULTS_PAGE = (By.CSS_SELECTOR, 'h2.title.title--primary')
    DUMMY_RESULTS_DROPDOWN = (By.CSS_SELECTOR, "div.predictive-search-results")

    def add_first_product_to_cart(self, *locator):
       # sleep(3)
        first_product = self.find_element(*self.ADD_1ST_TO_CART)
        actions = ActionChains(self.driver)
        actions.move_to_element(first_product)
        actions.perform()
        self.wait_until_element_click(*self.ADD_1ST_TO_CART)

    def verify_no_results_page(self, *locator):
        expected_result = 'No results'
        actual_result = self.driver.find_element(*self.DUMMY_RESULTS_PAGE).text
        assert expected_result in actual_result, f'Expected {expected_result}, but got {actual_result}'

    def verify_no_results_found(self):
        expected_result = self.driver.find_element(*self.SEARCH_RESULTS)
        actual_result = self.driver.find_element(*self.DUMMY_RESULTS_DROPDOWN)
        assert expected_result is not actual_result

    def verify_sun_protection_shown(self, expected_result):
        actual_result = self.driver.current_url
        assert expected_result in actual_result, f'Expected {expected_result}, but got {actual_result}'

    def verify_first_product(self, expected_result):
        actual_result = self.driver.find_element(*self.FIRST_PRODUCT).text
        assert expected_result in actual_result, f'Expected {expected_result}, but got {actual_result}'
