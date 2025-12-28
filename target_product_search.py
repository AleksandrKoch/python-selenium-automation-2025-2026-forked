#HW2 optional:
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


# Start Chrome browser
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(4)

# Open target.com
driver.get("https://www.target.com/")
sleep(1)

# Search for "Keyboard"
driver.find_element(By.ID, "search").send_keys("Keyboard")
driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()

#Verify search results
expected_text = "Keyboard"
actual_text = driver.find_element(By.XPATH, "//div[contains(@class, 'styles_listingPageResultsCountWrapper')]").text

assert expected_text in actual_text, f"Expected query {expected_text} not in {actual_text}"
sleep(2)