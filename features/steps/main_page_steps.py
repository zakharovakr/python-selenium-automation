from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

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
    sleep(6)

@when('Click on Cart icon')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartIcon']").click()
    sleep(3)

@when('Click on Add to cart button for the first item found')
def click_add_cart_button_for_first_item(context):
    buttons = context.driver.find_elements(By.XPATH, "//button[text()='Add to cart']")
    buttons[0].click()
    sleep(3)

@when('Click on Add to cart button on right side menu')
def click_add_cart_button_side_menu(context):
    context.driver.find_element(By.CSS_SELECTOR, "button[data-test='shippingButton']").click()

@when('Click on View cart and checkout button')
def click_view_cart_button(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href='/cart']").click()

@then('Validate Added to cart text is shown')
def validate_added_to_cart_text(context):
    expected_text = 'Added to cart'
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "h2[data-test='modal-drawer-heading'] span[class*='text']").text
    assert expected_text in actual_text, f'Expected text {expected_text} is not in actual text {actual_text}'

@when('Click Sign In')
def click_sign_in(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']").click()

@when('From right side navigation menu, click Sign In')
def click_sign_in_side_menu(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()
    sleep(3)