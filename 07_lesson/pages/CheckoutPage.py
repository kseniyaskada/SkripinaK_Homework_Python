from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    def __init__(self, driver):
        self._driver = driver

    def input_info(self, name, lastname, zipcode):

        self._driver.find_element(
            By.CSS_SELECTOR, '#first-name').send_keys(name)
        self._driver.find_element(
            By.CSS_SELECTOR, '#last-name').send_keys(lastname)
        self._driver.find_element(
            By.CSS_SELECTOR, '#postal-code').send_keys(zipcode)

        self._driver.find_element(By.CSS_SELECTOR, '#continue').click()

    def find_price(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(EC.url_contains('checkout-step-two'))

        total_price = self._driver.find_element(
            By.CSS_SELECTOR, '.summary_total_label')

        total_text = total_price.text

        return float(total_text.split('$')[1])
