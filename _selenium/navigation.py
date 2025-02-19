from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time
#This example requires Selenium WebDriver 3.13 or newer
url = "https://google.com/ncr"
driver = webdriver.Chrome()
driver.get(url)
search = driver.find_element(By.NAME,"q").send_keys("cheese" + Keys.ENTER)
time.sleep(3)
driver.close()
# with webdriver.Chrome() as driver:
#     wait = WebDriverWait(driver, 10)
#     driver.get("https://google.com/ncr")
#     driver.find_element(By.NAME, "q").send_keys("cheese" + Keys.RETURN)
# time.sleep(3)
# driver.close()