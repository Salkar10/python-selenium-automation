from selenium.webdriver.common.by import By

from pages.base_page import Page


class CartPage(Page):
    CART_EMPTY_MSG = (By.XPATH,'//*[@class="styles_ndsHeading__HcGpD styles_fontSize1__i0fbt styles_x2Margin__M5gHh"]')

    def verify_cart_empty_msg(self):
        expected_text = 'Your cart is empty'
        actual_text = self.driver.find_element(*self.CART_EMPTY_MSG).text
        assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'