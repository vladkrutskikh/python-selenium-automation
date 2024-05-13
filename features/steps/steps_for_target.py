from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target page')
def open_target(context):
    context.driver.get('https://www.target.com/')
    sleep(6)


@when('Click on Cart icon')
def click_on_cart_icon(context):
    context.driver.find_element(By.XPATH, "//div[@data-test='@web/CartIcon']").click()
    sleep(6)


@then("Verify 'Your cart is empty' message is shown")
def verify_cart_is_empty(context):
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "h1[class*='StyledHeading']").text
    expected_text = 'Your cart is empty'
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'


@when("Click Sign In")
def click_sign_in(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']").click()
    sleep(4)


@when("From right side navigation menu, click Sign In")
def click_sign_in(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()
    sleep(4)


@then("Verify Sign In form opened")
def verify_sign_in_form_opened(context):
    context.driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']")
    context.driver.find_element(By.ID, 'username')
    context.driver.find_element(By.ID, 'password')
    print('Test case passed.')
