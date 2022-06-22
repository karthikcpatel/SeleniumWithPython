from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

chromeOptions = Options()
chromeOptions.add_experimental_option("prefs",{"download.default_directory":"C:\selenium with python"})
driver = webdriver.Chrome('./chromedriver',options=chromeOptions)
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chromeOptions)
driver.implicitly_wait(30)
driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()
#download text file
driver.find_element(By.ID,"textbox").send_keys("KP downloading apple file")
driver.find_element(By.ID,"createTxt").click()
driver.find_element(By.ID,"link-to-download").click()
time.sleep(5)
print("Successfully downloaded text file")
#download pdf file
driver.execute_script("window.scrollBy(0,500)","")
driver.find_element(By.ID,"pdfbox").send_keys("KP downloading apple file")
time.sleep(5)
driver.find_element(By.ID,"createPdf").click()
driver.find_element(By.ID,"pdf-link-to-download").click()
time.sleep(5)
print("Successfully downloaded pdf file")
driver.close()