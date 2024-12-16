import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

@pytest.fixture
def browser():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield
    browser.quit()

@pytest.mark.order(1)
def test_login_functionality(browser):
    browser.get("https://example.com/login")
    assert "Login" in browser.title

@pytest.mark.order(2)
def test_search_functionality(browser):
    browser.get("https://example.com")
    search_box = browser.find_element("name", "q")
    search_box.send_keys("pytest")
    search_box.submit()
    assert "Search Results" in browser.title

@pytest.mark.order(3)
def test_logout_functionality(browser):
    browser.get("https://example.com/logout")
    assert "Logged Out" in browser.title
