from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time

@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    driver.close()

def test_go_to_page(test_setup):
    driver.get("https://www.python.org")
    print(driver.title)
    time.sleep(5)

# def test_teardown(test_setup):
#     driver.quit()