# This represents the right-side drawer / sidenav

from selenium.webdriver.common.by import By
from pages.base_page import Page


class AccountMenu(Page):
    # Drawer container (broad but stable)
    DRAWER = (By.XPATH, "//div[@role='dialog' or @aria-modal='true']")

    # "Sign in" button or link
    SIGN_IN_BTN = (By.CSS_SELECTOR, "[data-test='accountNav-signIn']")

    def wait_until_opened(self):
        self.wait_until_element_present(*self.DRAWER)

    def click_sign_in(self):
        self.wait_until_clickable_click(*self.SIGN_IN_BTN)
