from behave import given, when, then
from app.application import Application
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


@then('Verify that the cart is empty')
def verify_empty_cart(context):
    context.app.cart_page.verify_empty_cart()
