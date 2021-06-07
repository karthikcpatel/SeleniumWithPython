from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chromeOptions = Options()
chromeOptions.add_experimental_option("prefs",{"download.default_directory":"C:\selenium with python"})
driver = webdriver.Chrome('./chromedriver',options=chromeOptions)
driver.implicitly_wait(30)
driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()
#download text file
driver.find_element_by_id("textbox").send_keys("KP downloading apple file")
driver.find_element_by_id("createTxt").click()
driver.find_element_by_id("link-to-download").click()
time.sleep(2)
print("Successfully downloaded text file")
#download pdf file
driver.execute_script("window.scrollBy(0,500)","")
driver.find_element_by_id("pdfbox").send_keys("KP downloading apple file")
time.sleep(3)
driver.find_element_by_id("createPdf").click()
driver.find_element_by_id("pdf-link-to-download").click()
time.sleep(2)
print("Successfully downloaded pdf file")
driver.close()