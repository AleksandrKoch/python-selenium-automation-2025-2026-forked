from selenium.webdriver.common.by import By

from pages.base_page import Page


class CartPage(Page):
    EMPTY_CART_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")
    empty_cart_msg = 'Your cart is empty'

    TOTAL_TXT = (By.CSS_SELECTOR, "h2 [class*='styles_cart-summary-span']")
    PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='cartItem-title']")

    def open_cart_page(self):
        self.open_url('/cart')

    def verify_empty_cart_msg(self):
        self.verify_partial_text(self.empty_cart_msg, *self.EMPTY_CART_MSG)

    def wait_until_loaded(self):
        self.wait_until_element_present(*self.TOTAL_TXT)

    def verify_items_count(self, amount):
        """
        amount comes from step as string, e.g. "1"
        We'll parse it here to keep steps clean.
        """
        self.wait_until_loaded()
        amount = int(amount)

        # Two options to implement this depending on your DOM:
        # Option 1 (recommended): if there is a locator for "X items" text, add it here and parse it.
        # Option 2 (fallback): count line items in cart.

        # ---- FALLBACK example: count items ----
        CART_ITEMS = (By.CSS_SELECTOR, "[data-test='cartItem']")
        self.wait_until_element_present(*CART_ITEMS)
        items = self.find_elements(*CART_ITEMS)
        actual = len(items)

        assert actual == amount, f"Expected {amount} item(s) in cart, but got {actual}"

    def get_product_name(self):
        self.wait_until_element_present(*self.PRODUCT_NAME)
        return self.find_element(*self.PRODUCT_NAME).text

    def verify_product_matches(self, expected_name):
        actual_name = self.get_product_name()
        assert actual_name[:20] == expected_name[:20], \
            f"Expected product {expected_name[:20]} but got {actual_name[:20]}"