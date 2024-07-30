from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class SigninPage(Page):
    SIGNIN_BTN = (By.ID, 'login')
    SIGN_IN_HEADER = (By.CSS_SELECTOR, 'h1 span')
    TC_LINK = (By.CSS_SELECTOR, '[aria-label="terms & conditions - opens in a new window"]')


    def open_signin(self):
        self.open_url('https://www.target.com/login')
    def verify_signin_form(self):
        self.wait_for_element_appear(*self.SIGNIN_BTN)
        self.verify_text('Sign into your Target account', *self.SIGN_IN_HEADER)

    def click_tc_link(self):
        self.click(*self.TC_LINK)