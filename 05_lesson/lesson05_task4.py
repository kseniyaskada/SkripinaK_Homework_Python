from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/login")

wait = WebDriverWait(driver, 10)

search_field = "#username"
search_input = driver.find_element(By.CSS_SELECTOR, search_field)
search_input.send_keys("tomsmith")
search_field_sec = "#password"
search_input_sec = driver.find_element(By.CSS_SELECTOR, search_field_sec)
search_input_sec.send_keys("SuperSecretPassword!")

select_button = driver.find_element(By.CSS_SELECTOR, 'i')
select_button.click()


find_text = wait.until(EC.visibility_of_element_located
                       ((By.CSS_SELECTOR, '#flash')))
print("Текст с зелёной плашки:")
print(find_text.text)

driver.quit()
