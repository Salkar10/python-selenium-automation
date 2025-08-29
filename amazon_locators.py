from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Get the path to the ChromeDriver executable
# ChromeDriverManager will download and manage the ChromeDriver for you
driver_path = ChromeDriverManager().install()

# Create a new Chrome browser service
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Open the target URL
driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to='
    'https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity='
    'http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle='
    'usflex&openid.mode=checkid_setup&openid.claimed_id='
    'http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns='
    'http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')




#Amazon Logo
driver.find_element(By.XPATH, '//*[@class="a-icon a-icon-logo"]')


#Email Field
driver.find_element(By.ID, "ap_email")


# Continue button
driver.find_element(By.ID, "continue" )


# Conditions of Use link
driver.find_element(By.XPATH, '//*[@href="/gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use?ie=UTF8&nodeId=508088"]')


# Privacy Notice link
driver.find_element(By.XPATH, '//*[@href="/gp/help/customer/display.html/ref=ap_signin_notification_privacy_notice?ie=UTF8&nodeId=468496"]')


# "Need help?" expander
driver.find_element(By.XPATH, '//*[@class="a-expander-prompt"]')


# Forgot Password link
driver.find_element(By.ID, "auth-fpp-link-bottom")


# Other Sign-in issues link
driver.find_element(By.ID, "ap-other-signin-issues-link")


# Create account button
driver.find_element(By.ID, "createAccountSubmit")





sleep(10)
driver.quit()