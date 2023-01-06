from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://seleniumpractise.blogspot.com/2021/08/webtable-in-html.html")
scroll_to_table = driver.find_element(By.XPATH,"//table[@id='customers']/preceding-sibling::h2")
driver.execute_script("arguments[0].scrollIntoView();",scroll_to_table)
table = driver.find_element(By.XPATH,"//table[@id='customers']")
rows = table.find_elements(By.TAG_NAME,"tr")

for i in range(0,len(rows)):
    columns = rows[i].find_elements(By.TAG_NAME,"td")

    for j in range(0,len(columns)):
        if columns[j].text == "Amazon":
            select_checkbox = columns[j].text
            #driver.find_element(By.XPATH,"//input[@type='checkbox']").click()
            #driver.find_element(By.XPATH, "//table[@id='customers']/tbody/tr["+i+"]/td["+j+"]//input[@type='checkbox']").click()
            driver.find_element(By.XPATH,"//td[text()='"+select_checkbox+"']//preceding-sibling::td//input[@type='checkbox']").click()
            time.sleep(3)

driver.close()