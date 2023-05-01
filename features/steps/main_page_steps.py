from behave import given, when, then
from app.application import Application
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains


@given('Open main page')
def open_cureskin(context):
    context.app.main_page.open_main_page()


@when('Select sunscreens')
def select_sunscreens(context):
    context.app.header.select_sunscreens()


@when('Close pop up window')
def close_pop_up(context):
    context.app.main_page.close_pop_up()
    # context.driver.find_element(By.CSS_SELECTOR, '.popup-close').click()
