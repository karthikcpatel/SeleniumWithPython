import moment
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.python.org")
print(driver.title)
screenshot_name = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
print(screenshot_name)
driver.save_screenshot("C:\\Users\\kartik.patel\\PycharmProjects\\SeleniumWithPython\\web selenium\\screenshots\\"+screenshot_name+".png")
driver.close()