import moment
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service

chrome_driver=Service(r'C:\Users\kartik.patel\PycharmProjects\SeleniumWithPython\web selenium\chromedriver.exe')
driver = webdriver.Chrome(service=chrome_driver)
driver.get("https://www.python.org")
print(driver.title)
screenshot_name = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
print(screenshot_name)
driver.get_screenshot_as_file("C:\\Users\\kartikp\\PycharmProjects\\Selenium_Python\\web selenium\\screenshots\\"+screenshot_name+".png")
driver.close()