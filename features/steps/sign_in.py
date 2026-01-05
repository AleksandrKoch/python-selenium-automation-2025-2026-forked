# HW3.3
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Sign in form opened')
def verify_sign_in_form(context):
    assert "Sign in or create account" in context.driver.find_element(By.CSS_SELECTOR, "h1.styles_ndsHeading__phw6r").text,\
        "Sign in form did not open"


