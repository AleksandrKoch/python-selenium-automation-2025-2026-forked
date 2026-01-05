# HW3.2
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target main page')
def open_target_main_page(context):
    context.driver.get('https://www.target.com')
    sleep(1)


@when('Click on cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()
    sleep(1)


@then('Empty cart message is shown')
def verify_empty_cart_message(context):
    # assert "Your cart is empty" in context.driver.page_source
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").text
    assert "Your cart is empty" in actual_text, f"Expected text 'Your cart is empty' not found in {actual_text}"
    sleep(1)