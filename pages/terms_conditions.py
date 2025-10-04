from pages.base_page import Page

class TermsConditions(Page):


     def verify_tc_opened(self):

        self.wait_until_url_contains('target_terms_conditions')
