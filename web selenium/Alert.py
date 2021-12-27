from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service

chrome_driver=Service('C:/Users/kartik.patel/Downloads/chromedriver.exe')
driver = webdriver.Chrome(service=chrome_driver)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
print("Successfully maximized the window")
time.sleep(5)

driver.find_element("//button[@onclick='myFunction()']").click()
time.sleep(3)
driver.switch_to.alert.accept()
print("Successfully clicked ok")

driver.find_element("//*[@id='HTML9']/div[1]/button").click()
time.sleep(3)
driver.switch_to.alert.dismiss()
print("Successfully clicked dismiss")

driver.close()