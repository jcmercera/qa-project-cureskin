from selenium.webdriver.common.by import By
from selenium import webdriver
from pages.base_page import Page


class Header(Page):
    SHOP_BY_PRODUCTS = (By.XPATH,
                        "//summary[@class='header__menu-item header__menu-item--top list-menu__item focus-inset']/span[contains(text(),'Shop by Product')]")
    SUNSCREENS = (By.XPATH, "//span[contains(text(),'Sunscreens')]")
    SEARCH_ICON = (By.CSS_SELECTOR, 'svg.icon.icon-search.modal__toggle-open')
    SEARCH_FIELD = (By.CSS_SELECTOR, "input.search__input.field__input[aria-controls='predictive-search-results-list']")
    PREDICTIVE_SEARCH_ICON = (
    By.CSS_SELECTOR, 'button.predictive-search__item--term.button.button--small.button--full-width')

    #    HEADER_BLOCK =
    #    SIGN_IN_BUTTON =
    #    CART_ICON =
    #    HAM_MENU =

    def click_on_shop_by_product(self, *locator):
        self.find_element(*self.SHOP_BY_PRODUCTS).click()

    def select_sunscreens(self, *locator):
        self.find_element(*self.SUNSCREENS).click()

    def click_on_search_icon(self, *locator):
        self.find_element(*self.SEARCH_ICON).click()

    def click_on_search(self, *locator):
        self.find_element(*self.PREDICTIVE_SEARCH_ICON).click()

    def search_for_product(self, *product_name):
        self.find_element(*self.SEARCH_FIELD).click()
        self.input_text(product_name, *self.SEARCH_FIELD)
