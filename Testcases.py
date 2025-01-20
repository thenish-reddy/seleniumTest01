from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyotp
import time

def login_to_salesforce(driver, username, password, secret_key):
    wait = WebDriverWait(driver, 10)
    driver.get("https://sitetracker-ericssonglobal-eu01.my.salesforce.com/?ec=302&startURL=%2Fvisualforce%2Fsession%3Furl%3Dhttps%253A%252F%252Fsitetracker-ericssonglobal-eu01.lightning.force.com%252Flightning%252Fr%252Fsitetracker__Project__c%252Fa0i2x000002Zoo3AAC%252Fview")

    # SSO Login
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="idp_section_buttons"]/button'))).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="i0116"]'))).send_keys(username)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="idSIButton9"]'))).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="i0118"]'))).send_keys(password)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="idSIButton9"]'))).click()

    # Handle OTP
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="signInAnotherWay"]'))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="idDiv_SAOTCS_Proofs"]/div[2]/div/div/div[2]/div'))).click()

    totp = pyotp.TOTP(secret_key)
    current_otp = totp.now()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="idTxtBx_SAOTCC_OTC"]'))).send_keys(current_otp)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="idSubmit_SAOTCC_Continue"]'))).click()

    menu_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[1]/section/div[1]/div[1]/one-appnav/div/div/div/div/one-app-launcher-header/button/div')))
    menu_button.click()
    # Navigate to "Sites"
    driver.refresh()
    driver.refresh()
    menu_in_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[1]/section/div[1]/div[1]/one-appnav/div/div/div/div/one-app-launcher-header/button/div')))
    menu_in_button.click()
    time.sleep(2)
    menu_viewall_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content_502:0"]/one-app-launcher-menu/div/lightning-button')))
    menu_viewall_button.click()
    time.sleep(3)
    site_field = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="input-107"]')))
    site_field.send_keys('sites')
    site_in_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="lgt-accordion-section-113"]/slot/ul/li/one-app-launcher-tab-item/a/span/lightning-formatted-rich-text/span/p/mark')))
    site_in_button.click()
    driver.refresh()
    sitenew_in_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="brandBand_1"]/div/div/div/div/div[1]/div[1]/div[2]/ul/li[1]/a/div')))
    sitenew_in_button.click()

    
