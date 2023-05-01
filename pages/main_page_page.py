from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from time import sleep
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains


class MainPage(Page):
    POP_UP_WINDOW = (By.CSS_SELECTOR, '.popup-close')

    def open_main_page(self):
        self.open_url('https://shop.cureskin.com/')
        sleep(2)

    def close_pop_up(self):
        sleep(3)
        close_pop_up = self.find_element(*self.POP_UP_WINDOW)
        actions = ActionChains(self.driver)
        actions.move_to_element(close_pop_up).perform()
        self.wait_for_element_appear(*self.POP_UP_WINDOW).click()
