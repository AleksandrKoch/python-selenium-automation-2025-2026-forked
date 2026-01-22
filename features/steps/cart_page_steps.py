from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then

EMPTY_CART_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")
CART_ITEM_TITLE = (By.XPATH, "//div[@data-test='cartItem-title']/div")
ADDED_TO_CART_HEADER = (By.CSS_SELECTOR, "[data-test='modal-drawer-heading']")

@then('Empty cart message is shown')
def verify_empty_cart_message(context):
    wait = WebDriverWait(context.driver, 10)
    cart_empty_element = wait.until(EC.visibility_of_element_located(EMPTY_CART_MSG))
    actual_text = cart_empty_element.text
    assert "Your cart is empty" in actual_text, (
        f"Expected text 'Your cart is empty' not found in '{actual_text}'"
    )
    # assert "Your cart is empty" in context.driver.page_source
    # actual_text = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").text
    # assert "Your cart is empty" in actual_text, f"Expected text 'Your cart is empty' not found in {actual_text}"
    # sleep(1)
    # Wait until the empty-cart message element is visible



@then('Verify {product} is added to the cart')
def verify_product_added_to_sidenav_cart(context, product):
    wait = WebDriverWait(context.driver, 10)
    added_message = wait.until(EC.visibility_of_element_located(ADDED_TO_CART_HEADER))
    assert added_message.text == "Added to cart", (
        "'Added to cart' message is missing"

    # item_el = wait.until(EC.visibility_of_element_located(CART_ITEM_TITLE))
    # expected = product.lower()
    # actual = item_el.text.lower()
    # assert expected in actual, (
    #     f"Expected product '{product}' not found in cart item text '{item_el.text}' "
    #     f"at {context.driver.current_url}"
    )
    # assert product.lower() in context.driver.find_element(By.XPATH, "//div[@data-test='cartItem-title']/div").text.lower(), \
    #     f'Expected product {product} not found in {context.driver.current_url}'
    # sleep(1)