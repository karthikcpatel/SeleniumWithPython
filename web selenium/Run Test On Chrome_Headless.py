from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

option=Options()
option.add_argument("--headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=option)
driver.get("https://www.python.org")
print(driver.title)
driver.close()