from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.redbus.in/")
driver.find_element(By.ID,"onward_cal").click()
time.sleep(2)
table = driver.find_element(By.XPATH,"//div[@id='rb-calendar_onward_cal']//table")
tr = driver.find_elements(By.TAG_NAME,"tr")
for i in range(0,len(tr)):
    print(tr[i].text)
    if tr[i].text == "30":
        driver.find_element(By.XPATH, "//td[text()=30]").click()
    #td = tr[i].find_elements(By.TAG_NAME,"td")
    #for j in range(0,len(td)):
        #if td[j].text == "30":
            #driver.find_element(By.XPATH, "//td[text()=30]").click()

    #if tr[i].text == "30":
        #driver.find_element(By.XPATH,"//td[text()=30]").click()
        #print("Clicked successfully")
    #td = tr[i].find_elements(By.TAG_NAME,"td")
    #for j in range(0,len(td)):
        #if td[i].text == "30":
            #driver.find_element(By.XPATH,"//tr[@class='rb-monthHeader']//following-sibling::tr[j]/td").click()
            #print(td[j].text)