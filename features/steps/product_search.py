from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



@given('Open Target page')
def open_target(context):
    context.driver.get('https://www.target.com/')
    sleep(5)




@when('Click on search icon')
def click_search_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, 'id="search').send_keys('gloves')
    context.driver.find_element(By.CSS_SELECTOR, '//button[@data-test="@web/Search/SearchButton"]').click()


    sleep(6)


@then('Verify search results are shown')
def verify_search_results(context):
    actual_text = context.driver.find_element(By.CSS_SELECTOR, '//div[@data-test="lp-fulfillmentFilterBar"]').text
    expected_text = 'Gloves'
    assert expected_text in actual_text, f'Error. Expected text {expected_text}'

