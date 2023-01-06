from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://jqueryui.com/droppable/")
driver.maximize_window()
time.sleep(5)
driver.execute_script("window.scrollBy(0,200)","")
driver.switch_to.frame(0)

from_element = driver.find_element(By.ID, "draggable")
to_element = driver.find_element(By.ID, "droppable")

actions = ActionChains(driver)
actions.drag_and_drop(from_element,to_element).perform()
print("Successfully dragged and dropped the element")

time.sleep(3)
driver.close()

print("********** Second Approach **********")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://jqueryui.com/droppable/")
driver.maximize_window()
time.sleep(5)
driver.execute_script("window.scrollBy(0,200)","")
driver.switch_to.frame(0)

element = driver.find_element(By.ID, "draggable")

actions = ActionChains(driver)
#actions.drag_and_drop(from_element,to_element).perform()
actions.drag_and_drop_by_offset(element,100,15).perform()
print("Successfully dragged and dropped the element using offset method")

time.sleep(3)
driver.close()
