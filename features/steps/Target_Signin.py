
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Get the path to the ChromeDriver executable
# ChromeDriverManager will download and manage the ChromeDriver for you
driver_path = ChromeDriverManager().install()

# Create a new Chrome browser service
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()


from behave import given, when, then

#Start Chrome browser:
ACCOUNT_ICON = (By.XPATH, '//*[@class="sc-b1397f11-3 deTpgY h-margin-r-x3"]')
SIGN_IN_BTN = (By.XPATH, '//*[@data-test=accountNav-signIn')
SIGN_IN_MSG = (By.XPATH,'//*[@class="styles_ndsHeading__HcGpD styles_fontSize1__i0fbt styles_x2Margin__M5gHh h-text-lg h-text-center h-margin-b-tiny"]')


@given('Open Target home page')
def open_target(context):
    context.driver.get('https://www.target.com/')



@when('click account icon in header')
def click_account_icon(context):
    #search = context.driver.find_element(By.XPATH,'//*[@class="sc-b1397f11-3 deTpgY h-margin-r-x3"]')
    #search.click()
    #search.send_keys()
    #sleep(5)
    context.app.header.click_account_icon()


@when('click on Sign in button')
def sign_in_button(context):
     #search = context.driver.find_element(By.XPATH,'//*[@data-test=accountNav-signIn')
     #search.click()
     #sleep(4)
    context.app.signin_page.click_sign_in_btn()

@then("Verify 'Sign in  {expected_text} message is shown'")
def verify_sign_in_msg(context, expected_text):
    #context.driver.find_element = (By.XPATH,'//*[@class="styles_ndsHeading__HcGpD styles_fontSize1__i0fbt styles_x2Margin__M5gHh h-text-lg h-text-center h-margin-b-tiny"]')
    #expected_text = 'sign in'
    actual_text = context.app.signin_page.text
    #assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'
    context.app.signin_page.verify_sign_in_msg(expected_text)

sleep(6)

print('test case passed')


