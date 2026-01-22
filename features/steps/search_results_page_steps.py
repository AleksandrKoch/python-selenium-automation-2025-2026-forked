from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then


SEARCH_RESULTS_TEXT = (By.XPATH, "//div[contains(@class,'styles_listingPageResultsCountWrapper___vvdK')]")
ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#addToCartButtonOrTextIdFor13010225")
SIDENAV_ADD_TO_CART = (By.CSS_SELECTOR, "[data-test='shippingButton']")
ORDER_PICKUP_BUTTON = (By.CSS_SELECTOR, "[data-test='orderPickupButton']")
SIDENAV_MODAL = (By.CSS_SELECTOR, ".ReactModal__Content")

@then('Search results for {search_word} are shown')
def verify_found_results_text(context, search_word):
    actual_text = context.driver.find_element(SEARCH_RESULTS_TEXT).text
    assert search_word.lower() in actual_text, \
        f'Expected query not in {context.driver.current_url.lower()}'


# @then('Verify tea is added to the cart')
# def verify_tea_is_added(context):


@when('Add product to the cart')
def add_product_to_cart(context):
    wait = WebDriverWait(context.driver, 10)

    wait.until(EC.element_to_be_clickable(ADD_TO_CART_BUTTON)).click()
    wait.until(EC.visibility_of_element_located(SIDENAV_MODAL))
    wait.until(EC.element_to_be_clickable(SIDENAV_ADD_TO_CART)).click()


