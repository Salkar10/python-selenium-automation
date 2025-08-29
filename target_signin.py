from multiprocessing.forkserver import SIGNED_STRUCT

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep



#Start Chrome browser:
driver_path = ChromeDriverManager().install()
driver = webdriver.Chrome(service=Service(driver_path))
driver.maximize_window()
driver.implicitly_wait(5)

# Open the target URL
driver.get('https://www.target.com/')



# Wait until the Account button is clickable and then click
#WebDriverWait(driver, 30).until(EC.element_to_be_clickable(...))


driver.find_element(By.XPATH, '//span[@class="sc-b1397f11-3 deTpgY h-margin-r-x3" and text()="Account"]').click()


# Step 3: Click Sign In button from side navigation
driver.find_element(By.XPATH,'//*[@data-test="accountNav-signIn"]').click()

# Step 4: Verify Sign In page opened
driver.find_element(By.XPATH, '//*[text()="Sign in or create account"]')

#Make sure login button is shown
login=driver.find_element(By.ID, 'login')

driver.quit()





