from behave import given, when, then
from features.pages.login_page import LoginPage
import time

@given("I open the Magento homepage")
def step_open_homepage(context):
    context.driver.get("https://magento.softwaretestingboard.com/")
    context.login_page = LoginPage(context.driver)
    time.sleep(2)

@when('I click the "Sign In" link')
def step_click_sign_in(context):
    context.login_page.click_sign_in_link()
    time.sleep(2)

@when('I enter email "{email}" and password "{password}"')
def step_enter_credentials(context, email, password):
    context.login_page.enter_email(email)
    context.login_page.enter_password(password)
    context.login_page.submit_login()
    time.sleep(2)

@then('I should see a welcome message with my name')
def step_verify_welcome_message(context):
    assert context.login_page.is_welcome_message_visible()
