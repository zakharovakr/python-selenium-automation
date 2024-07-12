from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open Target circle page')
def open_target(context):
    context.driver.get('https://www.target.com/circle')

@then('Verify the page has {number} benefit cells')
def verify_benefit_cells_count(context, number):
    number = int(number)
    cells = context.driver.find_elements(By.CSS_SELECTOR, "[data-test='@web/slingshot-components/CellsComponent/Link']")
    assert len(cells) == number, f'Expected {number} links but got {len(cells)}'