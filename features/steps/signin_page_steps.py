from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@then('Verify Sign In form opened')
def verify_sign_in_form(context):
    context.driver.find_element(By.ID, 'login')
    # verify “Sign into your Target account” text is shown
    expected_text = 'Sign into your Target account'
    actual_text = context.driver.find_element(By.XPATH, "//span[contains(text(), 'account')]").text
    # print(actual_text)
    assert expected_text in actual_text, f'Expected text {expected_text} is not in actual text {actual_text}'