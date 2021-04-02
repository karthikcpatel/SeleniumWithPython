from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest

def test_google():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.google.com")
    title = driver.title
    assert title == "Google"
    driver.close()

@pytest.mark.skip
def test_msn():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.msn.com/en-in")
    print(driver.title)
    driver.close()