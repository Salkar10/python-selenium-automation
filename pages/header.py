from time import sleep
from behave import given, when, then
from selenium.webdriver.common.by import By
from pages.base_page import Page

class Header(Page):
    CART_ICON = (By.XPATH, '//*[@data-test="@web/CartIcon"]')
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    ACCOUNT_ICON = (By.XPATH, '//*[@class="sc-b1397f11-3 deTpgY h-margin-r-x3"]')
    SIDE_NAV_CART_ICON = (By.CSS_SELECTOR, 'div[data-test="content-wrapper"] [id="addToCartButtonOrTextIdFor12946357"]')

#@when('Search for {search_word}')
    def search_product(self):
    #print('searching product')
       self.input_text('gloves', *self.SEARCH_FIELD)
       self.click(*self.SEARCH_BTN)
       sleep(9)
    #context.app.header.search_product()

    def click_cart(self):
       self.click(*self.CART_ICON)





#@when('click account icon in header')
    def click_account_icon(self):
       self.click(*self.ACCOUNT_ICON)
    #search = context.driver.find_element(By.XPATH,'//*[@class="sc-b1397f11-3 deTpgY h-margin-r-x3"]')
    #search.click()
    #search.send_keys()
    #sleep(5)


#@when('click cart button from side navigation')
    def side_nav_click_cart(self):
        self.driver.click(*self.SIDE_NAV_CART_ICON)