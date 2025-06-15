from selenium import webdriver

def before_all(context):
    # You can swap to Chrome, Firefox, etc.
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(5)

def after_all(context):
    context.driver.quit()
