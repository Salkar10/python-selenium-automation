from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
driver_path = ChromeDriverManager().install()

# Create a new Chrome browser service
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

from behave import given, when, then

#Start Chrome browser:


# open the url
@given('open target home page')
def open_search(context):
     context.driver.get('https://www.target.com/')



#Click:
@when('click on cart icon')
def click_cart(context):
    context.driver.find_element(By.XPATH,'//*[@data-test="@web/CartIcon"]')
    context.click()
    context.send_keys()
    sleep(5)


#verify
@then('Verify Your cart is empty {expected_text} is shown')
def verify_cart_empty_msg(context, expected_text):
    actual_text = context.driver.find_element(By.XPATH,'//*[@class="styles_ndsHeading__HcGpD styles_fontSize1__i0fbt styles_x2Margin__M5gHh"]').text
    expected_text = 'Your cart is empty'
    assert expected_text in actual_text, f"Expected '{expected_text}' but found '{actual_text}'"


print('test case passed')





