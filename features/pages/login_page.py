from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def click_sign_in_link(self):
        sign_in_link = self.driver.find_element(By.LINK_TEXT, "Sign In")
        sign_in_link.click()

    def enter_email(self, email):
        email_input = self.driver.find_element(By.ID, "email")
        email_input.send_keys(email)

    def enter_password(self, password):
        password_input = self.driver.find_element(By.ID, "pass")
        password_input.send_keys(password)

    def submit_login(self):
        login_btn = self.driver.find_element(By.ID, "send2")
        login_btn.click()

    def is_welcome_message_visible(self):
        try:
            welcome_element = self.driver.find_element(By.CSS_SELECTOR, "span.logged-in")
            return "Welcome" in welcome_element.text
        except:
            return False
