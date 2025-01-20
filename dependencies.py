import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from decouple import config

def get_driver():
    # BrowserStack credentials
    BROWSERSTACK_USERNAME = "thenu_fr1sIT"
    BROWSERSTACK_ACCESS_KEY = "rSfP7Y1VdcnwDMynND3Y"

    # Capabilities for BrowserStack
    capabilities = {
        'bstack:options': {
            'os': 'Windows',
            'osVersion': '10',
            'seleniumVersion': '4.0.0',
            'buildName': 'Automation Test',
            'browserName': 'chrome',
            'browserVersion': 'latest'
        }
    }

    chrome_options = Options()
    chrome_options.set_capability('bstack:options', capabilities['bstack:options'])

    # Initialize WebDriver
    driver = webdriver.Remote(
        command_executor=f'https://{BROWSERSTACK_USERNAME}:{BROWSERSTACK_ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub',
        options=chrome_options
    )

    return driver
