from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@then('Empty cart message is shown')
def verify_empty_cart_message(context):
    # assert "Your cart is empty" in context.driver.page_source
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").text
    assert "Your cart is empty" in actual_text, f"Expected text 'Your cart is empty' not found in {actual_text}"
    sleep(1)


