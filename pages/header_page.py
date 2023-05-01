from selenium.webdriver.common.by import By
from selenium import webdriver
from pages.base_page import Page
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from sample_script import driver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains


class Header(Page):
    SHOP_BY_PRODUCTS = (By.XPATH,
                        "//summary[@class='header__menu-item header__menu-item--top list-menu__item "
                        "focus-inset']/span[contains(text(),'Shop by Product')]")
    SUNSCREENS = (By.XPATH, "//span[contains(text(),'Sunscreens')]")
    SEARCH_ICON = (By.CSS_SELECTOR, 'svg.icon.icon-search.modal__toggle-open')
    SEARCH_FIELD = (By.CSS_SELECTOR, "input.search__input.field__input[aria-controls='predictive-search-results-list']")
    PREDICTIVE_SEARCH_ICON = (
        By.CSS_SELECTOR, 'button.predictive-search__item--term.button.button--small.button--full-width')
    CART_ICON = (By.ID, 'cart-icon-bubble')

    #    HEADER_BLOCK =
    #    SIGN_IN_BUTTON =
    #    CART_ICON =
    #    HAM_MENU =

    def click_on_shop_by_product(self, *locator):
        sleep(2)
        self.click(*self.SHOP_BY_PRODUCTS)

    def select_sunscreens(self, *locator):
        self.click(*self.SUNSCREENS)

    def click_on_search_icon(self, *locator):
        # self.wait_until_element_click(*self.SEARCH_ICON)
        sleep(1)
        self.wait_until_element_click(*self.SEARCH_ICON)

    def click_on_predict_search(self, *locator):
        sleep(1)
        self.click(*self.PREDICTIVE_SEARCH_ICON)

    def search_for_product(self, *product_name):
        self.wait_for_element_appear(*self.SEARCH_FIELD)
        self.input_text(product_name, *self.SEARCH_FIELD)

    def go_to_cart(self, *locator):
        self.click(*self.CART_ICON)
