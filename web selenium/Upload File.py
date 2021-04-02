from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(30)
driver.get("http://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.switch_to.frame(0)
driver.execute_script("window.scrollBy(0,1000)","")
time.sleep(2)
driver.find_element_by_id("RESULT_FileUpload-10").send_keys("C://Work/Others/All Important Documents/My Images/My Image.jpg")
time.sleep(2)
#driver.close()