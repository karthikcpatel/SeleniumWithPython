from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.python.org")
print(driver.title)
driver.close()