from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get(
            "https://bonigarcia.dev/"
            "selenium-webdriver-java/"
            "slow-calculator.html")
        self._driver.maximize_window()

    def delay_field_input(self):
        input = self._driver.find_element(By.CSS_SELECTOR, '#delay')
        input.clear()
        input.send_keys("45")

    def click_buttons(self):
        self._driver.find_element(By.XPATH, '//span[text()="7"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="+"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="8"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="="]').click()

    def wait_result(self):
        wait = WebDriverWait(self._driver, 45)
        wait.until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, ".screen"), "15"))

        screen = self._driver.find_element(By.CSS_SELECTOR, '.screen')

        return screen.text
