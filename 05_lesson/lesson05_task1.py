from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("http://uitestingplayground.com/classattr")

select_button = driver.find_element(By.CSS_SELECTOR, '.class3.btn-primary')
select_button.click()
