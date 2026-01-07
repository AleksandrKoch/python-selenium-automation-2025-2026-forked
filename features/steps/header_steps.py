from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_FIELD = (By.ID, "search")
SEARCH_ICON = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
HEADER_LINKS = (By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")


@when('Click on cart icon')
def click_cart_icon(context):
    context.driver.find_element(*CART_ICON).click()
    sleep(1)


@when('Search for {product}')
def search_product(context, product):
    context.driver.find_element(*SEARCH_FIELD).send_keys(product)
    context.driver.find_element(*SEARCH_ICON).click()


@when('User clicks Account button')
def click_account_button(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/AccountLink']").click()
    sleep(1)

@when('Sidenav opened')
def verify_sidenav_opened(context):
    assert "Sign in" in context.driver.find_element(By.CSS_SELECTOR, ".ReactModal__Content").text, \
        "Sidenav did not open"
    sleep(1)




@when('Click on Cart icon in Sidenav')
def click_cart_icon_sidenav(context):
    context.driver.find_element(By.XPATH, "//a[text()='View cart & check out']").click()
    sleep(1)

@then('User clicks Sign in button')
def verify_sign_in_button(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()
    sleep(1)


@then('Verify {expected_amount} top header links are shown')
def verify_top_links_shown(context, expected_amount):
    expected_amount = int(expected_amount) # convert parameter into integer
    links = context.driver.find_elements(*HEADER_LINKS)
    assert len(links) == expected_amount, f'Expected {expected_amount} links, but found {len(links)}'







