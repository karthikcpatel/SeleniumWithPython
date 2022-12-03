from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
# The below code exemplifies implicit wait
driver.implicitly_wait(10)
assert "Practice" in driver.title
# The below code exemplifies explicit wait
driver.get("https://www.google.com/")
wait = WebDriverWait(driver,10)
assert wait.until(EC.title_is("Google"))
time.sleep(2)
# The below code exemplifies fluent wait
driver.get("https://www.python.org")
wait = WebDriverWait(driver, timeout=10, poll_frequency=2, ignored_exceptions=[TimeoutException])
wait.until(EC.title_is("Welcome to Python.org"))
time.sleep(2)
driver.close()