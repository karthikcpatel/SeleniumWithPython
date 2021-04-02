from selenium import webdriver
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome('./chromedriver')
driver.get("https://jqueryui.com/droppable/")
driver.maximize_window()
time.sleep(5)

driver.execute_script("window.scrollBy(0,200)","")

driver.switch_to.frame(0)

from_element = driver.find_element_by_id("draggable")
to_element = driver.find_element_by_id("droppable")

actions = ActionChains(driver)
actions.drag_and_drop(from_element,to_element).perform()
print("Successfully dragged and dropped the element")

time.sleep(2)
driver.close()