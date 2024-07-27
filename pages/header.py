from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class Header(Page):
    SIGNIN_BTN = (By.XPATH, "//a[@data-test='@web/AccountLink']")
    SIDE_BAR_SIGNIN_BTN = (By.XPATH, "//a[@data-test='accountNav-signIn']")
    CART_BTN = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")

    def search_product(self, product):
        self.input_text(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        # wait for the page with search results to load
        sleep(6)

    def click_cart(self):
        self.wait_and_click(*self.CART_BTN)

    def click_sign_in(self):
        self.wait_and_click(*self.SIGNIN_BTN)

    def click_sign_in_from_side_bar(self):
        self.wait_and_click(*self.SIDE_BAR_SIGNIN_BTN)