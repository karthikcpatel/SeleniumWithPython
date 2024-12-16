from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest

@pytest.fixture
def test_browser():
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())  # or webdriver.Firefox(), etc.
    yield driver
    driver.quit()


@pytest.mark.parametrize("search_term", ["pytest", "selenium", "python"])
def test_search_functionality(test_browser, search_term):
    driver.get("https://www.google.com")
    search_box = driver.find_element("name", "q")
    search_box.send_keys(search_term)
    search_box.submit()

    assert search_term in test_browser.title



