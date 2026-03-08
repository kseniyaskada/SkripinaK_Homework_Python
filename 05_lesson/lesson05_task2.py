from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://uitestingplayground.com/dynamicid")

select_button = driver.find_element(By.CSS_SELECTOR, '.btn-primary')
select_button.click()
