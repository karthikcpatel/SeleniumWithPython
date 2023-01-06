from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://courses.letskodeit.com/practice")
driver.maximize_window()
time.sleep(5)

driver.execute_script("window.scrollBy(0,1000)")
time.sleep(3)

driver.switch_to.frame(0)
print("Successfully switched to iFrame")

driver.find_element(By.XPATH,"//div[@class='input-group']//following-sibling::input").send_keys("KP Testing")

time.sleep(3)

driver.switch_to.default_content()
print("Successfully switched to parent window")

driver.close()