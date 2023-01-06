from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(3)
driver.execute_script("window.scrollBy(0,1000)","")
table_text = driver.find_element(By.XPATH,"//tbody[1]")
print(table_text.text)
print("Successfully printed text from web table")
driver.quit()