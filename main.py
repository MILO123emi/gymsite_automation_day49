from selenium import webdriver
import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

load_dotenv()
URL = os.getenv("GYM_URL")
print(URL)
MAIL = os.getenv("AsaveCCOUNT_EMAIL")
PAS = os.getenv("ACCOUNT_PASSWORD")


user_dara_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument(f"--user-data-dir={user_dara_dir}")
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)
WebDriverWait(driver, 10)
driver.find_element(By.CSS_SELECTOR, "#main-navigation #login-button").click()
WebDriverWait(driver, 10)
driver.find_element(By.CSS_SELECTOR, "#login-form #email-input").send_keys(MAIL)