from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@then("Verify 'Your cart is empty' message is shown")
def verify_cart_is_empty(context):
    expected_text = 'Your cart is empty'
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "h1").text
    # print(actual_text)
    assert expected_text in actual_text, f'Expected text {expected_text} is not in actual text {actual_text}'
