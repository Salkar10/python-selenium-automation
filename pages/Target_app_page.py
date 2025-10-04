from selenium.webdriver.common.by import By

from pages.base_page import Page


class TargetAppPage(Page):

    TC_LINK = (By.CSS_SELECTOR, "[aria-label='terms & conditions - opens in a new window']")


    def open_target_sign_in_page(self):
        self.open_url('https://www.target.com/orders?lnk=acct_nav_my_account')
        #self.open_url('https://www.target.com/c/target-app/-/N-4th2r')


    def click_terms_conditions_link(self):
        self.click(*self.TC_LINK)
