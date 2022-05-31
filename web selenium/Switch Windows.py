from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("http://demo.automationtesting.in/Windows.html")
driver.implicitly_wait(10)
parent_window = driver.current_window_handle
driver.find_element(By.XPATH,"//*[@id='Tabbed']/a/button").click()

handles = driver.window_handles

for handle in handles:
    if handle != parent_window:
        driver.switch_to.window(handle)
        print(driver.title)
        driver.close()
        driver.switch_to.window(parent_window)
        print(driver.title)

driver.quit()
