from pages.cart_page import CartPage
from pages.header import Header
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.account_menu import AccountMenu
from pages.sign_in_page import SignInPage
from pages.add_to_cart_drawer import AddToCartDrawer

class Application:

    def __init__(self, driver):
        self.cart_page = CartPage(driver)
        self.main_page = MainPage(driver)
        self.header = Header(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.account_menu = AccountMenu(driver)
        self.sign_in_page = SignInPage(driver)
        self.add_to_cart_drawer = AddToCartDrawer(driver)