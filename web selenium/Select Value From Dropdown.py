from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.execute_script("window.scrollBy(0,250)","")
driver.find_element(By.XPATH,"//select[@name='speed']").click()
driver.find_element(By.XPATH,"//select[@name='speed']/option[3]").click()
time.sleep(3)
print("Successfully selected first value")
driver.close() #Successfully closed the driver.

print("********** Example 2 **********")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("C:/Users/kartik.patel/Downloads/Selenium%20Practice%20Form.html")
driver.maximize_window()
driver.execute_script("window.scrollBy(0,350)","")
driver.find_element(By.XPATH,"//select[@name='RESULT_RadioButton-9']").click()
driver.find_element(By.XPATH,"//select[@name='RESULT_RadioButton-9']/option[2]").click()
time.sleep(3)
driver.close() #Successfully closed the driver.