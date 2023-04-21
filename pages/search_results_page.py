from selenium.webdriver.common.by import By
from selenium import webdriver
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC
from sample_script import driver


# from selenium import EC

class SearchResults(Page):
    FIRST_PRODUCT = (By.CSS_SELECTOR, 'a.card-information__text.h4')

    def verify_sun_protection_shown(self, expected_result):
        actual_result = self.driver.current_url
        assert expected_result in actual_result, f'Expected {expected_result}, but got {actual_result}'
        # self.driver.current_url

    def verify_first_product(self, expected_result):
        actual_result = self.driver.find_element(*self.FIRST_PRODUCT).text
        assert expected_result in actual_result, f'Expected {expected_result}, but got {actual_result}'
