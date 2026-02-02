from selenium.webdriver.common.by import By
from pages.base_page import Page


class SignInPage(Page):
    # Common redirect domain for Target auth
    PARTIAL_URL = "target.com/login"

    # Optional: if I need a DOM proof too later
    # EMAIL_INPUT = (By.CSS_SELECTOR, "input[type='email']")

    def verify_opened(self):
        self.wait_until_url_contains(self.PARTIAL_URL)
        self.verify_url_contains(self.PARTIAL_URL)
