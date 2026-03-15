from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge()
driver.get("https://uitestingplayground.com/textinput")
input = driver.find_element(By.CSS_SELECTOR, "#newButtonName")

input.send_keys('SkyPro')

button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
button.click()

wait = WebDriverWait(driver, 10)
updated_button = wait.until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "#updatingButton"), "SkyPro")
    )

new_button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")

print(new_button.text)

driver.quit()
