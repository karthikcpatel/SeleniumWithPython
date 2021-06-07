from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Chrome('./chromedriver')
driver.maximize_window()
driver.get("https://learn.letskodeit.com/p/practice")

driver.implicitly_wait(60)
assert "Practice" in driver.title
driver.get("https://www.google.com/")
wait = WebDriverWait(driver,60)
assert wait.until(EC.title_is("Google"))

time.sleep(2)

driver.close()


# time.sleep = wait for x number of time
# implicit wait = wait for specific number of time
# dynamic wait = wait for a specific time with a specific condition