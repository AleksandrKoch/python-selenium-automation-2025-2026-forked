from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_INPUT = (By.NAME, 'q')
SEARCH_SUBMIT = (By.NAME, 'btnK')


@when('Click on search icon')
def click_search_icon(context):
    context.driver.find_element(*SEARCH_SUBMIT).click()
    sleep(1)


@when('Input {search_word} into search field')
def input_search(context, search_word):
    search = context.driver.find_element(*SEARCH_INPUT)
    search.clear()
    search.send_keys(search_word)
    sleep(4)


@when('Click on cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()
    sleep(1)


@when('Search for tea')
def search_product(context):
    context.driver.find_element(By.ID, "search").send_keys("tea")
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/SearchButton']").click()


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
