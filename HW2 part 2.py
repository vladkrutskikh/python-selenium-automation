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
driver.get('https://www.target.com/')

driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']").click()

sleep(6)

driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()

sleep(6)

text_shown = driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text

sleep(6)

driver.find_element(By.ID, 'login')

assert 'Sign into your Target account' in text_shown, f'Error! Text Sign into your Target account not in {text_shown}.'
print('Test case passed.')

#I put sleep timers because sometimes it crashes without them
