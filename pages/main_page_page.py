from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class MainPage(Page):
    POP_UP_WINDOW = (By.CSS_SELECTOR, '.popup-close')

    def open_main_page(self):
        self.open_url('https://shop.cureskin.com/')

    def close_pop_up(self):
        self.wait_for_element_click(*self.POP_UP_WINDOW)
