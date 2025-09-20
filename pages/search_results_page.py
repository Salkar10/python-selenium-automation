from selenium.webdriver.common.by import By
from pages.base_page import Page
from behave import given, when, then

class SearchResultsPage(Page):

    SEARCH_RESULTS_TXT = (By.XPATH, '//div[@data-test="lp-fulfillmentFilterBar"]')

#@then('Verify search results are shown for {product}')
def verify_search_results(self):
    actual_text = self.find_element(*self.SEARCH_RESULTS_TXT).text
    product = 'gloves'
    #context.app.search_results_page.verify_search_results()
    assert product in actual_text, f'Error. Expected "{product}", but found "{actual_text.text}"'

