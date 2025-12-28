from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

# Locators
# By ID
driver.find_element(By.ID, 'twotabsearchtextbox')

#By XPATH
driver.find_element(By.XPATH, '//input[@aria-label="Search Amazon"]')

#By many attributes
driver.find_element(By.XPATH, '//input[@class="nav-input nav-progressive-attribute" and @type="text"]')

#By text
driver.find_element(By.XPATH, "//span[text()='Hello, sign in'] and @class='nav-line-1 nav-progressive-content'")

# By attribute, partial match
driver.find_element(By.XPATH, "//a[contains(@aria-label, 'Choose a language for shopping in Amazon United States')]")

