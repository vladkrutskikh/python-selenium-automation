from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

sleep(6)
driver.find_element(By.XPATH,"//a[@id='nav-link-accountList']").click()
sleep(6)
driver.find_element(By.XPATH,"//span[@id='auth-create-account-link']").click()
sleep(6)

driver.find_element(By.XPATH,"//i[@class='a-icon a-icon-logo']")
driver.find_element(By.XPATH,"//h1[@class='a-spacing-small']")
driver.find_element(By.XPATH,"//input[@id='ap_customer_name']")
driver.find_element(By.XPATH,"//input[@id='ap_email']")
driver.find_element(By.XPATH,"//input[@id='ap_password']")
driver.find_element(By.XPATH,"//div[@class='a-alert-content']")
driver.find_element(By.XPATH,"//input[@id='ap_password_check']")
driver.find_element(By.XPATH,"//input[@id='continue']")
driver.find_element(By.XPATH,"//a[contains(@href, 'notification_condition_of_use')]")
driver.find_element(By.XPATH,"//a[contains(@href, 'notification_privacy_notice')]")
driver.find_element(By.XPATH,"//a[@class='a-link-emphasis'][contains(@href, 'signin')]")