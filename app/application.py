from pages.Signin_page import SignInPage

from pages.base_page import Page
from pages.cart_page import CartPage
from pages.header import Header
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage


class Application:



    def __init__(self, driver):

        self.sign_in_page = SignInPage(driver)

        self.driver = driver
        self.cart_page = CartPage(driver)
        self.page = Page(driver)
        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.search_results_page = SearchResultsPage(driver)