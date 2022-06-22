from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://courses.letskodeit.com/practice")
driver.maximize_window()
time.sleep(3)

#driver.find_element(By.XPATH,"//a[text()='https://courses.letskodeit.com/practice']").click()
table_text = driver.find_element("//table[@id='product']/tbody").text
print(table_text)
print("Successfully printed text from web table")
driver.quit()