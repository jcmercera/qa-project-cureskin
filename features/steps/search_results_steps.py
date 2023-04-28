from behave import given, when, then
from app.application import Application
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


@when('Hover over first product')
def hover_over_first_product(context):
    context.app.search_results_page.hover_over_first_product()


@when('Add the first product to Cart')
def add_first_product_to_cart(context):
    context.app.search_results_page.add_first_product_to_cart()


@when('Reduce the quantity of the product to zero')
def reduce_item_from_side_cart(context):
    context.app.cart_page.reduce_item_from_side_cart()




@then('Verify {expected_result} header is shown')
def verify_sun_protection_shown(context, expected_result):
    context.app.search_results_page.verify_sun_protection_shown(expected_result)


@then('Verify the fist product is {expected_result}')
def verify_first_product(context, expected_result):
    context.app.search_results_page.verify_first_product(expected_result)


@then('Verify No results found  message is shown')
def verify_no_results_page(context):
    context.app.search_results_page.verify_no_results_page()


@then('Verify No results returned on the drop-down')
def verify_no_results_found(context):
    context.app.search_results_page.verify_no_results_found()

# driver.find_element(By.XPATH, "locator"), f"Element is present"
# @then('Verify {expected_result} header is shown')
# def verify_sun_protection_shown(context, expected_result):
# context.app.search_results_page.verify_sun_protection_shown(expected_result)
