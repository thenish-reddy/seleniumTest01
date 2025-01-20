from dependencies import get_driver
from Testcases import login_to_salesforce
from decouple import config

USERNAME = config('APP_USERNAME')
PASSWORD = config('APP_PASSWORD')
SECRET_KEY = "26krycrrp6pbjc55"

def main():
    driver = get_driver()
    try:
        login_to_salesforce(driver, USERNAME, PASSWORD, SECRET_KEY)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
