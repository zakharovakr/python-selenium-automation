from pages.base_page import Page


class TermsConditionsPage(Page):

    def verify_tc_url(self):
        self.verify_partial_url('/terms-conditions')