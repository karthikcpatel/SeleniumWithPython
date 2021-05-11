from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')
driver.maximize_window()
driver.get("http://demo.automationtesting.in/Windows.html")
driver.implicitly_wait(10)
parent_window = driver.current_window_handle
driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()

handles = driver.window_handles

for handle in handles:
    if handle != parent_window:
        driver.switch_to.window(handle)
        print(driver.title)
    #driver.switch_to.window(handle)
    #print(driver.current_window_handle)
    #print(driver.title)
    #time.sleep(3)
    #driver.close()

driver.quit()
