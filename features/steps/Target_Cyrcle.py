from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from behave import given, when, then
from time import sleep


benefits_cells = (By.CSS_SELECTOR, '.cell-item-content')

@given('open Target Circle page')
def step_open_target_circle(context):
    context.driver.get('https://www.target.com/circle')
    sleep(4)

@then('Verify search results are shown for {benefits}')
def verify_search_results(context, benefits):
    actual_text = context.driver.find_elements(By.CSS_SELECTOR, ".cell-item-content").text
    assert benefits in actual_text, f'Error. Expected text {benefits} but got {actual_text}'
