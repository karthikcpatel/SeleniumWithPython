from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.google.com/")
driver.find_element(By.NAME,"q").send_keys("selenium with python")
driver.find_element(By.NAME,"btnK").click()
driver.find_element(By.XPATH,"//a//h3").click()
driver.close()