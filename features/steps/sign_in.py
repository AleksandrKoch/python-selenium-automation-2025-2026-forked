# HW3.3
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('User clicks Account button')
def click_account_button(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/AccountLink']").click()
    sleep(1)

@when('Sidenav opened')
def verify_sidenav_opened(context):
    assert "Sign in" in context.driver.find_element(By.CSS_SELECTOR, ".ReactModal__Content").text, \
        "Sidenav did not open"
    sleep(1)


@then('User clicks Sign in button')
def verify_sign_in_button(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()
    sleep(1)


@then('Sign in form opened')
def verify_sign_in_form(context):
    assert "Sign in or create account" in context.driver.find_element(By.CSS_SELECTOR, "h1.styles_ndsHeading__phw6r").text,\
        "Sign in form did not open"