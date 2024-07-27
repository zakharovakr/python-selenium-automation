from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@then('Verify Sign In form opened')
def verify_sign_in_form(context):
    context.app.signin_page.verify_signin_form()
