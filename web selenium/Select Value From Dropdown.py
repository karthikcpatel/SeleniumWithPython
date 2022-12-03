from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
print("Successfully maximized the window")
time.sleep(3)

driver.execute_script("window.scrollBy(0,250)","")
driver.find_element(By.XPATH,"//select[@name='speed']").click()
driver.find_element(By.XPATH,"//select[@name='speed']/option[1]").click()

time.sleep(2)
print("Successfully selected first value")

driver.close() #Successfully closed the driver.