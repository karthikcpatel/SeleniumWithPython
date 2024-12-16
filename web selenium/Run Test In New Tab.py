from selenium import webdriver
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("http://www.google.com/")
driver.implicitly_wait(60)
body = driver.find_element(By.TAG_NAME,"body")
driver.execute_script("window.open()")
# We can press Ctrl + Tab using the below line.
#driver.find_element(By.TAG_NAME,'body').send_keys(Keys.COMMAND + 't')
time.sleep(3)
driver.switch_to.window(driver.window_handles[1])
driver.get('http://stackoverflow.com/')
time.sleep(3)
driver.close()