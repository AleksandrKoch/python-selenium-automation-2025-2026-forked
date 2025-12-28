from selenium import webdriver
from selenium.webdriver.common.by import By


# Start Chrome browser
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(4)

# Open amazon.com
driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')

# Locators for the HW2 part 1:

# Amazon logo:
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")

# Email field
driver.find_element(By.ID, 'ap_email')

# Continue button
driver.find_element(By.XPATH, "//input[@class='a-button-input']")

# Conditions of use link
driver.find_element(By.XPATH, "//*[text()='Conditions of Use']")

# Privacy notice link
driver.find_element(By.XPATH, "//*[text()='Privacy Notice']")

# Need help link
driver.find_element(By.XPATH, "//a[contains(text(), 'Need help signing in?')]")

# Forgot your password link is no longer on the page

# Other issues with Sign-in link is no longer on the page

# Create your Amazon account button
createAccountSubmit = driver.find_element(By.ID, "createAccountSubmit")







