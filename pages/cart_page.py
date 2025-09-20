from selenium.webdriver.common.by import By

from pages.base_page import Page


class CartPage(Page):


    CART_EMPTY_MSG = (By.XPATH,'//*[@class="styles_ndsHeading__HcGpD styles_fontSize1__i0fbt styles_x2Margin__M5gHh"]')

    CART_HAS_ITEM = (By.CSS_SELECTOR,'[class="styles_cart-summary-span__4h9y1"]')

    def verify_cart_empty_msg(self):
        expected_text = 'Your cart is empty'
        actual_text = self.driver.find_element(*self.CART_EMPTY_MSG).text
        assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'



#@then('Verify cart has {amount} item(s)')
    def verify_cart_has_1_item(self):
        expected_text = 'cart has 1 item'
        actual_text = self.driver.find_element(*self.CART_HAS_ITEM).text
        assert expected_text == actual_text, f"Expected {expected_text}, but got {actual_text}"
