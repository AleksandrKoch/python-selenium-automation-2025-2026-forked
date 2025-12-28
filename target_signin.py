#HW2 part 2:
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


# Start Chrome browser
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(4)

# Open target.com
driver.get("https://www.target.com/")
sleep(1)

# CLick Account button:
driver.find_element(By.XPATH, "//*[text()='Account']").click()
sleep(1)
# Click SignIn btn from side navigation
driver.find_element(By.XPATH, "//*[@data-test='accountNav-signIn']").click()

# Verify SignIn page opened:
# “Sign in or create account” text is shown:
expected_text = "Sign in or create account"
actual_text = driver.find_element(By.XPATH, "//h1[contains(@class, 'styles_ndsHeading')]").text

if expected_text in actual_text:
    print("Test passed")
else:
    print("Test failed, sign in page text does not match expected")


sleep(2)
driver.quit()
