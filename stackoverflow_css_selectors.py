# Locators for stackoverflow signup page. Try to use a css selector if possible, otherwise xpath is ok too

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Start Chrome browser
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(4)

# Open stackoverflow signup page
driver.get("https://stackoverflow.com/users/signup")

# CSS selector for "Create your account" headline:
driver.find_element(By.CSS_SELECTOR, "h1.fs-headline1")

# CSS selector for Terms section:
driver.find_element(By.CSS_SELECTOR, "div.js-terms")

# CSS selector for Email input field:
driver.find_element(By.CSS_SELECTOR, "#email")

# CSS selector for Password input field:
driver.find_element(By.CSS_SELECTOR, "#password")

# CSS selector for Show password button:
driver.find_element(By.CSS_SELECTOR, "svg.js-show-password")

# CSS selector for Sign up button:
driver.find_element(By.CSS_SELECTOR, "#submit-button")

# CSS selector for Sign up with Google button:
driver.find_element(By.CSS_SELECTOR, "button.s-btn__google")

# CSS selector for Sign up with Github button:
driver.find_element(By.CSS_SELECTOR, "button.s-btn__github")

driver.quit()
