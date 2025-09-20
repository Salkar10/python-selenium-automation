from selenium.webdriver.common.by import By


from .base_page import Page

class SignInPage(Page):

    SIGN_IN_BTN = (By.XPATH,'//*[@data-test=accountNav-signIn')
    SIGN_IN_MSG = (By.XPATH,'//*[@class="styles_ndsHeading__HcGpD styles_fontSize1__i0fbt styles_x2Margin__M5gHh h-text-lg h-text-center h-margin-b-tiny"]')

    def click_sign_in_btn(self):
    #context.app.sign_in_btn.click.sign_in_btn()
      self.click(*self.SIGN_IN_BTN)



    def verify_sign_in_msg(self):
       expected_text = 'sign in'
       actual_text = self.driver.find_element(*self.SIGN_IN_MSG).text
       assert expected_text == actual_text, f"Expected '{expected_text}' but got'{actual_text}'"