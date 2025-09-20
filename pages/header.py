from time import sleep
from behave import given, when, then
from selenium.webdriver.common.by import By
from pages.base_page import Page

class Header(Page):
    CART_ICON = (By.XPATH, '//*[@data-test="@web/CartIcon"]')
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")

#@when('Search for {search_word}')
def search_product(self):
    #print('searching product')
          self.input_text('gloves', *self.SEARCH_FIELD)
          self.click(*self.SEARCH_BTN)
          sleep(9)
    #context.app.header.search_product()

def click_cart(self):
    self.click(*self.CART_ICON)


