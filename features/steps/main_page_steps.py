from behave import given, when, then
from app.application import Application
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


@given('Open main page')
def open_cureskin(context):
    context.app.main_page.open_main_url()


@when('Click on "Shop by product"')
def click_on_shop_by_product(context):
    context.app.header.click_on_shop_by_product()


@when('Select sunscreens')
def select_sunscreens(context):
    context.app.header.select_sunscreens()


@when('Close pop up window')
def close_pop_up(context):
    context.app.main_page.close_pop_up()
    # context.driver.find_element(By.CSS_SELECTOR, '.popup-close').click()


<<<<<<< HEAD
@then('Verify the fist product is {expected_result}')
def verify_first_product(context, expected_result):
    context.app.search_results_page.verify_first_product(expected_result)


# @then('Verify {expected_result} header is shown')
# def verify_sun_protection_shown(context, expected_result):
# context.app.search_results_page.verify_sun_protection_shown(expected_result)
=======
@then('Verify {expected_result} header is shown')
def verify_sun_protection_shown(context, expected_result):
    context.app.search_results_page.verify_sun_protection_shown(expected_result)


@then('Verify the fist product is {expected_result}')
def verify_first_product(context, expected_result):
    context.app.search_results_page.verify_first_product(expected_result)
>>>>>>> origin/main
