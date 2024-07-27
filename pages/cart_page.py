from selenium.webdriver.common.by import By

from pages.base_page import Page


class CartPage(Page):
    CART_EMPTY_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg'] h1")
    ORDER_SUMMARY = (By.CSS_SELECTOR, 'div[data-test="cart-order-summary"] div span')

    def verify_cart_empty(self):
        self.wait_for_element_appear(*self.CART_EMPTY_MSG)
        self.verify_text('Your cart is empty', *self.CART_EMPTY_MSG)

    def verify_item_in_cart(self):
        self.wait_for_element_appear(*self.ORDER_SUMMARY)
        self.verify_text('1 item', *self.ORDER_SUMMARY)