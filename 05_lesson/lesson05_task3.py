from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/inputs")

search_field = "input"
search_input = driver.find_element(By.CSS_SELECTOR, search_field)
search_input.send_keys("12345")
search_input.clear()
search_input.send_keys("54321")
driver.quit()
