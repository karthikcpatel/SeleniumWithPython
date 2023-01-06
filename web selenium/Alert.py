from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
print("Successfully maximized the window")
time.sleep(5)

driver.find_element(By.XPATH,"//div[@class='widget-content']//following-sibling::button[text()='Click Me']").click()
#driver.find_element("//div[@class='widget-content']//following-sibling::button[text()='Click Me']").click()
time.sleep(3)
driver.switch_to.alert.accept()
print("Successfully clicked ok")

driver.find_element(By.XPATH,"//div[@class='widget-content']//following-sibling::button[text()='Click Me']").click()
time.sleep(3)
driver.switch_to.alert.dismiss()
print("Successfully clicked dismiss")

driver.close() #Successfully closed the driver.