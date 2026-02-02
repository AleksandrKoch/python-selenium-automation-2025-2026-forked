from selenium.webdriver.common.by import By
from pages.base_page import Page


class AddToCartDrawer(Page):
    # MOVE your locators from steps.py into here:
    SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
    SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")

    def wait_until_ready(self):
        # drawer is ready when confirm button is clickable
        self.wait_until_clickable(*self.SIDE_NAV_ADD_TO_CART_BTN)

    def get_product_name(self):
        self.wait_until_element_present(*self.SIDE_NAV_PRODUCT_NAME)
        return self.find_element(*self.SIDE_NAV_PRODUCT_NAME).text

    def confirm_add_to_cart(self):
        self.wait_until_clickable_click(*self.SIDE_NAV_ADD_TO_CART_BTN)
