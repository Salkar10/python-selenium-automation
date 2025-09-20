
from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



# open the url
@given('Open cart page')
def open_search(context):
     context.driver.get('https://www.target.com/s?searchTerm=soda')


@when('click cart button from side navigation')
def side_nav_click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, 'div[data-test="content-wrapper"] [id="addToCartButtonOrTextIdFor12946357"]').click()
    context.app.header.side_nav_click_cart()

sleep(6)

@then('Verify cart has {amount} item(s)')
def verify_search_results(context, amount):
    cart_summary = context.driver.find_element(By.CSS_SELECTOR, '[class="styles_cart-summary-span__4h9y1"]').text
    assert f'{amount} item(s)' in cart_summary, f"Expected {amount} item(s) but got {cart_summary}"
    context.app.header.verify_cart_has_1_item(amount)

