from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

driver = webdriver.Chrome('./chromedriver')
driver.maximize_window()
driver.get("https://learn.letskodeit.com/p/practice")

driver.implicitly_wait(120)
assert "Practice" in driver.title

driver.get("https://www.google.com/")
wait = WebDriverWait(driver,120)
assert wait.until(EC.title_is("Google"))

time.sleep(2)

driver.close()