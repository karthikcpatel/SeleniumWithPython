from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest

@pytest.mark.smoke
def test_alert():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.maximize_window()
    print("Successfully maximized the window")
    time.sleep(5)

    driver.find_element_by_xpath("//*[@id='HTML9']/div[1]/button").click()
    time.sleep(3)
    driver.switch_to.alert.accept()
    print("Successfully clicked ok")

    driver.find_element_by_xpath("//*[@id='HTML9']/div[1]/button").click()
    time.sleep(3)
    driver.switch_to.alert.dismiss()
    print("Successfully clicked dismiss")

    driver.close()