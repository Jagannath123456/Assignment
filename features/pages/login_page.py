from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def click_sign_in_link(self):
        link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign In")))
        link.click()

    def enter_email(self, email):
        email_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "login[username]")))
        email_input.clear()
        if email:
            email_input.send_keys(email)

    def enter_password(self, password):
        pwd_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "login[password]")))
        pwd_input.clear()
        if password:
            pwd_input.send_keys(password)

    def submit_login(self):
        btn = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.action.login.primary")))
        btn.click()

    def get_error_message(self):
        try:
            err = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".message-error")))
            return err.text.strip()
        except:
            return None

    def is_welcome_message_visible(self):
        try:
            # wait for the greeting span that actually appears after login
            greet = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "span.logged-in"))
            )
            text = greet.text.strip()
            print(f"[INFO] Welcome message detected: '{text}'")
            return "Welcome" in text
        except Exception as e:
            print(f"[ERROR] Welcome message not found: {e}")
            return False

    def is_field_error_visible(self, field_name):
        # field_name: 'email' or 'pass'
        selector = f"#{field_name}-error"
        try:
            err = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
            return err.text.strip()
        except:
            return None

    def logout_if_logged_in(self):
        try:
            account_menu = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".customer-welcome"))
            )
            account_menu.click()
            sign_out = self.wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Sign Out"))
            )
            sign_out.click()
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign In")))
            print("[INFO] Logged out successfully before test.")
        except:
            print("[INFO] No active session found.")
