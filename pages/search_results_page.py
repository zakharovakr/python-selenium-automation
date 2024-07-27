from selenium.webdriver.common.by import By

from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULTS_TXT = (By.XPATH, "//div[@data-test='resultsHeading']")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
    SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, '[data-test="shippingButton"]')
    VIEW_CART = (By.CSS_SELECTOR, 'a[href="/cart"]')

    def verify_search_results(self, expected_product):
        self.verify_partial_text(expected_product, *self.SEARCH_RESULTS_TXT)

    def verify_product_in_url(self, expected_product):
        self.verify_partial_url(expected_product)

    def add_to_cart_first_item(self):
        self.click(*self.ADD_TO_CART_BTN)
        self.wait_and_click(*self.SIDE_NAV_ADD_TO_CART_BTN)
        self.wait_and_click(*self.VIEW_CART)



