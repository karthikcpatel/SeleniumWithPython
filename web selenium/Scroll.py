from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')
driver.get("https://learn.letskodeit.com/p/practice")
driver.maximize_window()
time.sleep(5)

driver.find_element_by_xpath("//a[text()='https://courses.letskodeit.com/practice']").click()

driver.execute_script("window.scrollBy(0,500)","")
print("Successfully scrolled till a specific pixel")

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
time.sleep(5)

india_flag = driver.find_element_by_xpath("//td[text()='India']/..")
driver.execute_script("arguments[0].scrollIntoView();",india_flag)
time.sleep(5)
print("Successfully scrolled till an element")

driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(3)
print("Successfully scrolled till end of the page")

driver.close()