from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(2)
element = driver.find_element(By.XPATH,"//*[@id='HTML10']/div[1]/button")
actions = ActionChains(driver)
actions.double_click(element).perform()
print("Successfully performed double click")
time.sleep(2)
driver.close()