# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Firefox()
# driver.get('https://www.saucedemo.com/')

# driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys('standard_user')
# driver.find_element(By.CSS_SELECTOR, '#password').send_keys('secret_sauce')

# driver.find_element(By.CSS_SELECTOR, '#login-button').click()

# wait = WebDriverWait(driver, 10)
# wait.until(EC.url_contains('inventory'))

# driver.find_element(
#     By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()

# driver.find_element(
#     By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()

# driver.find_element(
#     By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()

# driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link').click()

# driver.find_element(By.CSS_SELECTOR, '#checkout').click()

# driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys('Иван')

# driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys('Иванов')

# driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys('111000')

# driver.find_element(By.CSS_SELECTOR, '#continue').click()


# total = driver.find_element(By.CSS_SELECTOR, '.summary_total_label')

# total.text

# # как вычленить только цифры из всего текста поля?

# assert "58.29" in total

# print("Тест пройден: итоговая стоимость = 58.29")

# driver.quit()
