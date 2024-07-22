from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

SEARCH_RESULT_HEADER = (By.CSS_SELECTOR, "div[data-test='resultsHeading']")
SIGNIN_HEADER = (By.CSS_SELECTOR, "h1")
EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, "div[data-test='boxEmptyMsg']")

@given('Open Target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')

@then('Verify header in shown')
def verify_header_present(context):
    context.driver.find_element(By.CSS_SELECTOR, "[class*='utilityHeaderContainer']")

@then('Verify header has {number} links')
def verify_header_link_amount(context, number):
    number = int(number)  # convert str "6" ==> to int 6
    links = context.driver.find_elements(By.CSS_SELECTOR, "[id*='utilityNav']")
    assert len(links) == number, f'Expected {number} links but got {len(links)}'

@when('Search for {product}')
def search_product(context, product):
    # find search field and enter text
    context.driver.find_element(By.ID, 'search').send_keys(product)
    # click search
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    # wait for the page with search results to load
    # sleep(6)
    context.driver.wait.until(EC.visibility_of_element_located(SEARCH_RESULT_HEADER))

@when('Click on Cart icon')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartIcon']").click()
    # sleep(3)
    context.driver.wait.until(EC.visibility_of_element_located(EMPTY_CART_MESSAGE))

@when('Click Sign In')
def click_sign_in(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']").click()

@when('From right side navigation menu, click Sign In')
def click_sign_in_side_menu(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()
    # sleep(3)
    context.driver.wait.until(EC.visibility_of_element_located(SIGNIN_HEADER))