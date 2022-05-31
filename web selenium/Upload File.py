from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(30)
driver.get("http://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.switch_to.frame(0)
driver.execute_script("window.scrollBy(0,1000)","")
time.sleep(2)
driver.find_element(By.ID,"RESULT_FileUpload-10").send_keys("C://Work/Others/All Important Documents/My Images/My Image.jpg")
time.sleep(3)
#driver.close()