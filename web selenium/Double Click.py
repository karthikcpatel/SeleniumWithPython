from selenium import webdriver
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome('./chromedriver')
driver.get("http://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(5)

element = driver.find_element_by_xpath("//*[@id='HTML10']/div[1]/button")

actions = ActionChains(driver)
actions.double_click(element).perform()
print("Successfully performed double click")

time.sleep(3)
driver.close()