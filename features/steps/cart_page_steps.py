from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='cartItem-title']")
TOTAL_TXT = (By.CSS_SELECTOR, "h2 [class*='styles_cart-summary-span']")


@when('Open cart page')
def open_cart(context):
    context.app.cart_page.open_cart_page()


@then('Verify cart has {amount} item(s)')
def verify_cart_items(context, amount):
    context.app.cart_page.verify_items_count(amount)

    cart_summary = context.driver.find_element(*TOTAL_TXT).text
    assert f'{amount} item' in cart_summary, f"Expected {amount} items but got {cart_summary}"


@then('Verify product in cart is correct')
def verify_product(context):
    context.app.cart_page.verify_product_matches(context.product_before_adding)


@then('Empty Cart message is shown')
def verify_empty_cart_msg(context):
    context.app.cart_page.verify_empty_cart_msg()