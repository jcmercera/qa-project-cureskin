from selenium.webdriver.common.by import By
from selenium import webdriver
from pages.base_page import Page


class Header(Page):
    SHOP_BY_PRODUCTS = (By.XPATH, "//summary[@class='header__menu-item header__menu-item--top list-menu__item focus-inset']/span[contains(text(),'Shop by Product')]")
    SUNSCREENS = (By.XPATH, "//span[contains(text(),'Sunscreens')]")

#    SEARCH_BUTTON =
#    HEADER_BLOCK =
#    SIGN_IN_BUTTON =
#    CART_ICON =
#    HAM_MENU =


    def click_on_shop_by_product(self, *locator):
        self.find_element(*self.SHOP_BY_PRODUCTS).click()


    def select_sunscreens(self, *locator):
        self.find_element(*self.SUNSCREENS).click()

