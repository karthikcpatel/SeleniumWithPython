#1 - Navigate to https://www.flipkart.com/
#2 - Close the pop-up or click X on the pop-up
#3 - Hover mouse on Electronics
#4 - Hover mouse on Gaming
#5 - Hover mouse on Gaming Mouse and perform a click
#6 - Click Price - Low to High
#7 - Click on first item to see the product details
#8 - Validate name of the product and product list page (previous screen) and product detail page (current screen) is the same
#9 - Close child window and navigate to parent window
#10 - Fetch title of parent window and close parent window

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


#instantiatechrome browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#navigate to specific url
driver.get("https://www.flipkart.com/")
driver.implicitly_wait(10)
#maximizing the window
driver.maximize_window()
#closing the pop-up
driver.find_element(By.XPATH,"//button[contains(text(),'✕')]").click()
#wait = WebDriverWait(driver,10)
#assert wait.until(EC.visibility_of_element_located(By.XPATH,"//a[normalize-space()='Login']"))
actions = ActionChains(driver)
#Hover mouse towards Electronics
electronics_parent = driver.find_element(By.XPATH, "//div[contains(text(),'Electronics')]")
actions.move_to_element(electronics_parent).perform()
#Hover mouse towards Gaming
gaming_child = driver.find_element(By.XPATH, "//a[normalize-space()='Gaming']")
actions.move_to_element(gaming_child).perform()
#Hover mouse towards Gaming Mouse
gaming_mouse_grand_child = driver.find_element(By.XPATH, "//a[normalize-space()='Gaming Mouse']")
actions.move_to_element(gaming_mouse_grand_child).click().perform()
#Click on Price - Low to High
driver.find_element(By.XPATH,"//div[normalize-space()='Price -- Low to High']").click()
#Store text of first item
product_list = driver.find_element(By.XPATH,"(//div[@data-id='ACCFDEGKP9PQJCGF']//following-sibling::a)[1]").text
#Get parent window handle
parent_window = driver.current_window_handle
#Click on first item
driver.find_element(By.XPATH,"(//div[@class='CXW8mj'])[1]").click()
#Get all active window handles
handles = driver.window_handles

for handle in handles:
    if handle != parent_window:
        driver.switch_to.window(handle)
        product_detail = driver.find_element(By.XPATH,"//span[@class='B_NuCI']").text
        #Check if text of item in product detail is available on product list
        if product_list in product_detail:
            print("The product name matches")
        driver.close()
        driver.switch_to.window(parent_window)
        print(driver.title)

driver.close()