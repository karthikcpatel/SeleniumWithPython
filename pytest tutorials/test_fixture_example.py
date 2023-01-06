from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pytest
import time

@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield
    driver.close()

def test_go_to_myntra(test_setup):
    driver.get("https://www.myntra.com/")
    print(driver.title)
    time.sleep(2)

def test_go_to_flipkart(test_setup):
    driver.get("https://www.flipkart.com/")
    print(driver.title)
    time.sleep(2)

def test_go_to_amazon(test_setup):
    driver.get("https://www.amazon.in/")
    print(driver.title)
    time.sleep(2)