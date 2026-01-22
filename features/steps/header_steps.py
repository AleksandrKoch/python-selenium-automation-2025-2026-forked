from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then


SEARCH_FIELD = (By.ID, "search")
SEARCH_ICON = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
HEADER_LINKS = (By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")
ACCOUNT_LINK = (By.CSS_SELECTOR, "[data-test='@web/AccountLink']")
SIDENAV_MODAL = (By.CSS_SELECTOR, ".ReactModal__Content")
SIDENAV_VIEW_CART = (By.XPATH, "//a[normalize-space()='View cart & check out']")
SIGN_IN_BUTTON = (By.CSS_SELECTOR, "[data-test='accountNav-signIn']")

@when('Click on cart icon')
def click_cart_icon(context):
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.element_to_be_clickable(CART_ICON)).click()

    wait.until(EC.url_contains("/cart"))

    # context.driver.find_element(*CART_ICON).click()
    # sleep(1)


@when('Search for {product}')
def search_product(context, product):
    wait = WebDriverWait(context.driver, 10)
    field = wait.until(EC.element_to_be_clickable(SEARCH_FIELD))
    field.send_keys(product)
    wait.until(EC.element_to_be_clickable(SEARCH_ICON)).click()

    # context.driver.find_element(*SEARCH_FIELD).send_keys(product)
    # context.driver.find_element(*SEARCH_ICON).click()


@when('User clicks Account button')
def click_account_button(context):
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.element_to_be_clickable(ACCOUNT_LINK)).click()
    wait.until(EC.visibility_of_element_located(SIDENAV_MODAL))

    # context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/AccountLink']").click()
    # sleep(1)

@when('Sidenav opened')
def verify_sidenav_opened(context):
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.text_to_be_present_in_element(SIDENAV_MODAL, "Sign in"))

    modal_text = context.driver.find_element(*SIDENAV_MODAL).text
    assert "Sign in" in modal_text, "Sidenav did not open"

    # assert "Sign in" in context.driver.find_element(By.CSS_SELECTOR, ".ReactModal__Content").text, \
    #     "Sidenav did not open"
    # sleep(1)


@when('Click on Cart icon in Sidenav')
def click_cart_icon_sidenav(context):
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.element_to_be_clickable(SIDENAV_VIEW_CART)).click()

    wait.until(EC.url_contains("/cart"))

    # context.driver.find_element(By.XPATH, "//a[text()='View cart & check out']").click()
    # sleep(1)


@then('User clicks Sign in button')
def verify_sign_in_button(context):
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.element_to_be_clickable(SIGN_IN_BUTTON)).click()

    # context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()
    # sleep(1)


@then('Verify {expected_amount} top header links are shown')
def verify_top_links_shown(context, expected_amount):
    wait = WebDriverWait(context.driver, 10)
    expected_amount = int(expected_amount) # convert parameter into integer

    links = wait.until(EC.presence_of_all_elements_located(HEADER_LINKS))

    assert len(links) == expected_amount, (
        f'Expected {expected_amount} links, but found {len(links)}'
    )







