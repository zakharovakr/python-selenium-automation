from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open sign in page')
def verify_open_signin_page(context):
    context.app.signin_page.open_signin()

@then('Verify Sign In form opened')
def verify_sign_in_form(context):
    context.app.signin_page.verify_signin_form()

@when('Click on Target terms and conditions link')
def click_tc_link(context):
    context.app.signin_page.click_tc_link()

@then('Verify Terms and Conditions page is opened')
def verify_tc_page_open(context):
    context.app.terms_conditions_page.verify_tc_url()

