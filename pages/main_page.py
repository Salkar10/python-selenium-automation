from behave import given, when, then
from pages.base_page import Page
from selenium.webdriver.common.by import By



class MainPage(Page):

#@given('open target main page')
      def open_main(self):
          self.open_url('https://www.target.com/')
          #context.app.main_page.open_main()



