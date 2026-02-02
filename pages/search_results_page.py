from selenium.webdriver.common.by import By

from pages.base_page import Page

class SearchResultsPage(Page):
    SEARCH_RESULTS_TEXT = (By.XPATH, "//div[contains(@class,'styles_listingPageResultsCount')]")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")

    def verify_search_results(self, expected_product):
        self.verify_partial_text(expected_product, *self.SEARCH_RESULTS_TEXT)

    def click_first_add_to_cart(self):
        # clicks first Add to cart on results
        self.wait_until_clickable_click(*self.ADD_TO_CART_BTN)