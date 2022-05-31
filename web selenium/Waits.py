from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://courses.letskodeit.com/practice")
driver.implicitly_wait(60)
assert "Practice" in driver.title
driver.get("https://www.google.com/")
wait = WebDriverWait(driver,60)
assert wait.until(EC.title_is("Google"))
time.sleep(2)
driver.close()