from pages.cart_page import CartPage
from pages.header import Header
from pages.help_page import HelpPage
from pages.main_page import MainPage
from pages.base_page import Page
from pages.privacy_policy_page import PrivacyPage
from pages.search_results_page import SearchResultsPage
from pages.signin_page import SigninPage
from pages.target_app_page import TargetAppPage
from pages.terms_conditions_page import TermsConditionsPage


class Application:
    def __init__(self, driver):

        self.base_page = Page(driver)

        self.cart_page = CartPage(driver)
        self.header = Header(driver)
        self.help_page = HelpPage(driver)
        self.main_page = MainPage(driver)
        self.privacy_page = PrivacyPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.signin_page = SigninPage(driver)
        self.target_app_page = TargetAppPage(driver)
        self.terms_conditions_page = TermsConditionsPage(driver)