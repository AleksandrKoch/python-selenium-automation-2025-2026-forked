from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_RESULTS_TEXT = (By.XPATH, "//div[contains(@class,'styles_listingPageResultsCountWrapper___vvdK')]")


@then('Search results for {search_word} are shown')
def verify_found_results_text(context, search_word):
    actual_text = context.driver.find_element(SEARCH_RESULTS_TEXT).text
    assert search_word.lower() in actual_text, \
        f'Expected query not in {context.driver.current_url.lower()}'


@when('Add product to the cart')
def add_product_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "#addToCartButtonOrTextIdFor17327543").click()
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='orderPickupButton']").click()
    sleep(2)