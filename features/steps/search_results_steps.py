from selenium.webdriver.common.by import By
from behave import then, when, given
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
@then('Verify search results shown for {expected_product}')
def verify_search_results(context, expected_product):
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert expected_product in actual_text, f'Expected {expected_product} not in actual {actual_text}'

@then('Verify correct search results URL opens for {expected_product}')
def verify_url(context, expected_product):
    url = context.driver.current_url
    assert expected_product in url, f'Expected {expected_product} not in {url}'

@when('Click on Add to cart button for the first item found')
def click_add_cart_button_for_first_item(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()  # always clicks on 1st Add to cart btn
    # buttons = context.driver.find_elements(By.XPATH, "//button[text()='Add to cart']")
    # buttons[0].click()
    context.driver.wait.until(EC.visibility_of_element_located(SIDE_NAV_PRODUCT_NAME))

@when('Store product name')
def store_product_name(context):
    context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
    print(f'Product stored: {context.product_name}')

@when('Click on Add to cart button on right side menu')
def click_add_cart_button_side_menu(context):
    # context.driver.find_element(By.CSS_SELECTOR, "button[data-test='shippingButton']").click()
    context.driver.find_element(*SIDE_NAV_ADD_TO_CART_BTN).click()

@when('Click on View cart and checkout button')
def click_view_cart_button(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href='/cart']").click()

@then('Validate Added to cart text is shown')
def validate_added_to_cart_text(context):
    expected_text = 'Added to cart'
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "h2[data-test='modal-drawer-heading'] span[class*='text']").text
    assert expected_text in actual_text, f'Expected text {expected_text} is not in actual text {actual_text}'