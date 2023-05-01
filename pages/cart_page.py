from selenium.webdriver.common.by import By
from selenium import webdriver
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC
from sample_script import driver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains


class CartPage(Page):
    QUANT_MIN_BUTTON = (By.CSS_SELECTOR, "button[name='minus']")
    EMPTY_CART_TEXT = (By.XPATH, "//h3[@class='mini-cart__empty-text'][text()='Your cart is currently empty']")

    def reduce_item_from_side_cart(self, *locator):
        quantity_button = self.find_element(*self.QUANT_MIN_BUTTON)
        actions = ActionChains(self.driver)
        actions.move_to_element(quantity_button)
        actions.perform()
        self.click(*self.QUANT_MIN_BUTTON)

    def verify_empty_cart(self):
        sleep(3)
        self.verify_text('Your cart is currently empty', *self.EMPTY_CART_TEXT)
