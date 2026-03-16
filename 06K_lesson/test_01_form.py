# from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form():

    driver = webdriver.Edge()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # заполнить поля значениями ->

    first_name = driver.find_element(
        By.CSS_SELECTOR, '[name="first-name"]').send_keys("Иван")

    last_name = driver.find_element(
        By.CSS_SELECTOR, '[name="last-name"]').send_keys("Петров")

    address = driver.find_element(
        By.CSS_SELECTOR, '[name="address"]').send_keys("Ленина, 55-3")

    mail = driver.find_element(
        By.CSS_SELECTOR, '[name="e-mail"]').send_keys("test@skypro.com")

    p_number = driver.find_element(
        By.CSS_SELECTOR, '[name="phone"]').send_keys("+7985899998787")

    city = driver.find_element(
        By.CSS_SELECTOR, '[name="city"]').send_keys("Москва")

    country = driver.find_element(
        By.CSS_SELECTOR, '[name="country"]').send_keys("Россия")

    job_position = driver.find_element(
        By.CSS_SELECTOR, '[name="job-position"]').send_keys("QA")

    company = driver.find_element(
        By.CSS_SELECTOR, '[name="company"]').send_keys("SkyPro")

    zip_code = driver.find_element(By.CSS_SELECTOR, '[name="zip-code"]')  # найти и задать переменную, не выполняя никаких действий

    driver.find_element(By.CSS_SELECTOR, 'button').click()  # нажать submit

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".alert")))  # <----- ??????????????????? ждем .alert (принятие формой данных, явное ожидание)

    element = driver.find_element(By.CSS_SELECTOR, '#zip-code').get_attribute('class')

    assert "alert-danger" in element, f'Пришел {element}'

    elements = ['first-name', 'last-name', 'address', 'e-mail', 'phone', 'city', 'country', 'job-position', 'company']

    for e in elements:
        element = driver.find_element(By.CSS_SELECTOR, f'[name="{e}"]')
        class_attr = element.get_attribute('class')
        assert 'alert-success' in class_attr, f"Элемент '{e}' не имеет класса 'alert-success'. Текущий класс: '{class_attr}'"

    driver.quit()
