from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from behave import given, when, then
from time import sleep
# from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
#driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.wait = WebDriverWait(driver, 10)



@given('Open Target page')
def open_target(context):
    context.driver.get('https://www.target.com/')




@when('Search for a product')
def search_product(context):

    search_input = context.driver.find_element(By.ID, 'search')
    search_input.send_keys('gloves')

    search_button = context.driver.find_element(By.XPATH, '//button[@data-test="@web/Search/SearchButton"]')
    search_button.click()


    sleep(6)


@then('Verify search results are shown')
def verify_search_results(context):
    actual_text = context.driver.find_element(By.CSS_SELECTOR, '//div[@data-test="lp-fulfillmentFilterBar"]').text
    expected_text = 'Gloves'
    assert expected_text in actual_text, f'Error. Expected text {expected_text}'

