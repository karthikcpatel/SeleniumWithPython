from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.python.org")
print(driver.title)
driver.close()

print("********** Example 2 **********")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.yahoo.com/")
print(driver.title)
driver.close()