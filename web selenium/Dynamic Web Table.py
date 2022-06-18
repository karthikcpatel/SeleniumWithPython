from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://seleniumpractise.blogspot.com/2021/08/webtable-in-html.html")
### Perform a click by writing a dynamic xPath
#driver.find_element(By.XPATH,"//td[text()='Ola']//preceding-sibling::td/input[@type='checkbox']").click()
#driver.find_element(By.XPATH,"")
scroll_to_table = driver.find_element(By.XPATH,"//table[@id='customers']/preceding-sibling::h2")
driver.execute_script("arguments[0].scrollIntoView();",scroll_to_table)
table = driver.find_element(By.XPATH,"//table[@id='customers']")

rows = table.find_elements(By.TAG_NAME,"tr")
print("Number of rows are: " + str(len(rows)))
columns = table.find_elements(By.TAG_NAME,"td")
print("Number of columns are: " + str(len(columns)))
for i in range(len(rows)):
    columns = rows[i].find_element(By.TAG_NAME,"td")
    for j in range(len(columns)):
        if columns[j].text == "Ola":
            columns[0].click()

time.sleep(5)
#before_xpath = "//td[text()="
#after_xpath = "]//preceding-sibling::td/input[@type='checkbox']"

#driver.find_element(By.XPATH,"//td[text()='Ola']//following-sibling::td[3]/a").click()
driver.close()