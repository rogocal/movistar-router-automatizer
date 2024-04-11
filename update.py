from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from dotenv import load_dotenv
import os

# Load and check if variables are loaded successfully
load_dotenv()
password = os.getenv("PASSWORD")
dns = os.getenv("DNS")
if password is None or dns is None:
    print("Error: Make sure PASSWORD and DNS are set in the .env file.")
else:
    print("PASSWORD:", password)
    print("DNS:", dns)

# Initialize the Chrome webdriver
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('--disable-infobars')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=options)

try:
    driver.get("http://192.168.1.1/te_red_local.asp")
    sleep(2)
    driver.find_element(By.NAME, "Password").send_keys(password)
    sleep(1)
    login_button = driver.find_element(By.CLASS_NAME, "te_acceso_router_enter")
    driver.execute_script("arguments[0].scrollIntoView(true);", login_button)
    login_button.click()
    sleep(1)
    driver.find_element(By.NAME, "DNSserver1").clear()
    driver.find_element(By.NAME, "DNSserver1").send_keys(dns)
    sleep(1)
    save_button = driver.find_element(By.CSS_SELECTOR, "td:nth-child(1) > input")
    driver.execute_script("arguments[0].scrollIntoView(true);", save_button)
    save_button.click()
    sleep(1)
    driver.close()
    print("DNS values updated successfully.")
    
except Exception as e:
    print("An error occurred:", e)

finally:
    # Close the browser window
    driver.quit()
