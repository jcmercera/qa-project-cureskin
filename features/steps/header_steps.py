from behave import given, when, then
from app.application import Application
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


@when('Click on "Shop by product"')
def click_on_shop_by_product(context):
    context.app.header.click_on_shop_by_product()


@when('Click on search icon')
def click_on_search_icon(context):
    context.app.header.click_on_search_icon()


@when('Click on search')
def click_on_search(context):
    context.app.header.click_on_search()


@when('Search for {product_name}')
def search_for_product(context, product_name):
    context.app.header.search_for_product(product_name)
