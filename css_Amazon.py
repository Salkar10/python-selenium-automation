from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Start Chrome browser
driver = webdriver.Chrome()
driver.maximize_window()

# Open the Amazon URL
driver.get('https://www.amazon.com/ap/register?openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&showRememberMe=true&openid.pape.max_auth_age=0&pageId=usflex&prepopulatedLoginId=&openid.assoc_handle=usflex&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fs%2F%3F_encoding%3DUTF8%26hvadid%3D604493509419%26hvdev%3Dc%26hvdvcmdl%3D%26hvexpln%3D0%26hvlocint%3D%26hvlocphy%3D9032063%26hvnetw%3Dg%26hvocijid%3D16363546094836408069--%26hvpone%3D%26hvpos%3D%26hvptwo%3D%26hvqmt%3Db%26hvrand%3D16363546094836408069%26hvtargid%3Dkwd-374536113546%26hydadcr%3D23962_13539148%26ie%3DUTF8%26index%3Daps%26keywords%3Damazon%2520website%2520login%26mcid%3Dee6249687364354abca9092fbf8955d2%26ref%3Dpd_sl_5xms72z3e6_b%26tag%3Dgooghydr-20%26ref_%3Dnav_custrec_newcust&policy_handle=Retail-Checkout')

#CSS selector using attributes
driver.find_element(By.CSS_SELECTOR,'[aria-label="www.amazon.com"]')


#Using class
driver.find_element(By.CSS_SELECTOR,'.a-spacing-small')

#using ID
driver.find_element(By.CSS_SELECTOR,"#ap_email")





sleep(10)
#Using class





cart_empty = (By.CSS_SELECTOR, "styles_ndsHeading__HcGpD styles_fontSize1__i0fbt styles_x2Margin__M5gHh")

