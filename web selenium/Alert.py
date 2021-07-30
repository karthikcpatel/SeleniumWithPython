from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
print("Successfully maximized the window")
time.sleep(5)

driver.find_element_by_xpath("//button[@onclick='myFunction()']").click()
time.sleep(3)
driver.switch_to.alert.accept()
print("Successfully clicked ok")

driver.find_element_by_xpath("//*[@id='HTML9']/div[1]/button").click()
time.sleep(3)
driver.switch_to.alert.dismiss()
print("Successfully clicked dismiss")

driver.close()