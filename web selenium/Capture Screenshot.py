from selenium import webdriver
import moment

driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.python.org")
print(driver.title)
#amit = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
screenshot_name = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
driver.get_screenshot_as_file("C:/Users/kartikp/PycharmProjects/Selenium_Python/web selenium/screenshots/"+screenshot_name+".png")
driver.close()