from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge()
driver.get("https://uitestingplayground.com/ajax")
driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

wait = WebDriverWait(driver, 20)

find_text = wait.until(EC.visibility_of_element_located
                       ((By.CSS_SELECTOR, '.bg-success')))
print(find_text.text)

driver.quit()
