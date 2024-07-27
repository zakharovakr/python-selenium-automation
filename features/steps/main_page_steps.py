from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

SEARCH_RESULT_HEADER = (By.CSS_SELECTOR, "div[data-test='resultsHeading']")
SIGNIN_HEADER = (By.CSS_SELECTOR, "h1")
EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, "div[data-test='boxEmptyMsg']")

@given('Open Target main page')
def open_target(context):
    context.app.main_page.open()

@then('Verify header in shown')
def verify_header_present(context):
    context.driver.find_element(By.CSS_SELECTOR, "[class*='utilityHeaderContainer']")


@then('Verify can click every link')
def verify_click_links(context):
    links = context.driver.find_elements(By.CSS_SELECTOR, "[id*='utilityNav']")

    for i in range(len(links)):
        # Search for links again because their internal IDs changed:
        # to avoid Stale Element Exception
        links = context.driver.find_elements(By.CSS_SELECTOR, "[id*='utilityNav']")
        print(f'Clicking on link {links[i].text}')
        links[i].click()
        sleep(4)

@when('Search for {product}')
def search_product(context, product):
    context.app.header.search_product(product)
@when('Click on Cart icon')
def click_cart(context):
    context.app.header.click_cart()

@when('Click Sign In')
def click_sign_in(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']").click()

@when('From right side navigation menu, click Sign In')
def click_sign_in_side_menu(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()
    # sleep(3)
    context.driver.wait.until(EC.visibility_of_element_located(SIGNIN_HEADER))