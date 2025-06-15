from behave import given, when, then
from features.pages.login_page import LoginPage

@given("I open the Magento homepage")
def step_open_homepage(context):
    context.driver.get("https://magento.softwaretestingboard.com/")
    context.login_page = LoginPage(context.driver)
    context.login_page.logout_if_logged_in()

@when('I click the "Sign In" link')
def step_click_sign_in(context):
    context.login_page.click_sign_in_link()

@when('I enter email "{email}" and password "{password}"')
def step_enter_credentials(context, email, password):
    context.email = email
    context.password = password
    context.login_page.enter_email(email)
    context.login_page.enter_password(password)
    context.login_page.submit_login()

@then('I should see outcome "{outcome}"')
def step_verify_outcome(context, outcome):
    lp = context.login_page
    context.expected_outcome = outcome  # store expected

    actual_outcome = "unknown"
    try:
        if outcome == 'success':
            result = lp.is_welcome_message_visible()
            actual_outcome = "success" if result else "failure"
            assert result, "Expected welcome message, but it was not visible."

        elif outcome == 'invalid_credentials':
            msg = lp.get_error_message()
            actual_outcome = "invalid_credentials" if msg and 'Invalid login or password' in msg else msg or "no error"
            assert 'Invalid login or password' in msg, f"Expected invalid credentials error, got: {msg}"

        elif outcome == 'required_email':
            err = lp.is_field_error_visible('email')
            actual_outcome = "required_email" if err and 'required' in err.lower() else err or "no error"
            assert 'required' in err.lower(), f"Expected email required error, got: {err}"

        elif outcome == 'required_password':
            err = lp.is_field_error_visible('pass')
            actual_outcome = "required_password" if err and 'required' in err.lower() else err or "no error"
            assert 'required' in err.lower(), f"Expected password required error, got: {err}"

        elif outcome == 'required_both':
            em = lp.is_field_error_visible('email')
            pw = lp.is_field_error_visible('pass')
            actual_outcome = "required_both" if em and pw and 'required' in em.lower() and 'required' in pw.lower() else f"{em}, {pw}"
            assert 'required' in em.lower() and 'required' in pw.lower(), \
                f"Expected both field errors, got email: {em}, pass: {pw}"

        elif outcome == 'invalid_email_format':
            msg = lp.get_error_message()
            actual_outcome = "invalid_email_format" if msg and 'email' in msg.lower() else msg or "no error"
            assert 'email' in msg.lower(), f"Expected invalid email format error, got: {msg}"

        elif outcome == 'weak_password':
            msg = lp.get_error_message()
            actual_outcome = "weak_password" if msg and 'short' in msg.lower() else msg or "no error"
            assert 'short' in msg.lower(), f"Expected weak password error, got: {msg}"

        else:
            raise AssertionError(f"Unknown outcome: {outcome}")

        context.actual_outcome = actual_outcome
        context.status = "PASS" if actual_outcome == outcome else "FAIL"

    except AssertionError as e:
        context.actual_outcome = actual_outcome
        context.status = "FAIL"
        raise e
