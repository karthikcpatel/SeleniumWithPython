from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')
driver.get("https://learn.letskodeit.com/p/practice")
driver.maximize_window()
time.sleep(5)

driver.find_element_by_xpath("//a[text()='https://courses.letskodeit.com/practice']").click()

driver.execute_script("window.scrollBy(0,800)","")
print("Successfully scrolled till a specific pixel")

table_text = driver.find_element("//table[@id='product']").text
print(table_text)
print("Successfully printed text from web table")

time.sleep(3)
driver.close()