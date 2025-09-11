
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



@given('Open Target home page')
def open_target(context):
    context.driver.get('https://www.target.com/')



@when('click account icon in header')
def click_account_icon(context):
    search = context.driver.find_element(By.XPATH,'//*[@class="sc-b1397f11-3 deTpgY h-margin-r-x3"]')
    search.click()
    search.send_keys()
    sleep(5)


@when('click on Sign in button')
def sign_in_button(context, ):
     context.driver.find_element(By.XPATH,'//*[@data-test=accountNav-signIn').click()
sleep(4)

@then('Sign in  {expected_text} message is shown')
def verify_sign_in_button(context, expected_text):
    actual_text = context.driver.find_element(By.XPATH,  '//*[@class="styles_ndsHeading__HcGpD styles_fontSize1__i0fbt styles_x2Margin__M5gHh h-text-lg h-text-center h-margin-b-tiny"]')
    assert expected_text in actual_text, f"Expected '{expected_text}' but found '{actual_text}'"



print('test case passed')


