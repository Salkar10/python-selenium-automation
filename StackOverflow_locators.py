from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Get the path to the ChromeDriver executable
# ChromeDriverManager will download and manage the ChromeDriver for you
driver_path = ChromeDriverManager().install()

# Create a new Chrome browser service
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://stackoverflow.com/users/signup')

#wait for page to load

driver.find_element(By.CSS_SELECTOR, '.flex--item.fs-headline1.fw-bold.lh-xs.mb8.ws-nowrap')

driver.find_element(By.CSS_SELECTOR, '.flex--item.js-terms.fs-caption.fc-black-400.ta-left')

driver.find_element(By.CSS_SELECTOR,'#email')

driver.find_element(By.CSS_SELECTOR,'#password')

driver.find_element(By.CSS_SELECTOR,'#submit-button')

driver.find_element(By.CSS_SELECTOR,'.flex--item.s-btn.s-btn__icon s-btn__google.bar-md.ba.bc-black-225')

driver.find_element(By.CSS_SELECTOR,'.flex--item.s-btn.s-btn__icon.s-btn__github.bar-md.ba.bc-black-225')


sleep(10)
driver.quit()