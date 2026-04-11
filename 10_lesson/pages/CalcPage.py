import allure
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

    @allure.step("Ввести число 45 в поле для ввода времени ожидания")
    def delay_field_input(self) -> None:
        """
        Вводит в поле для ввода времени ожидания число 45
        """
        input = self._driver.find_element(By.CSS_SELECTOR, '#delay')
        input.clear()
        input.send_keys("45")

    @allure.step(
            "Нажать на кнопки  '7', '+', '8' и '=' по очереди соответственно")
    def click_buttons(self) -> None:
        """
        Нажимает на цифры калькулятора в определенной последовательности
        """
        self._driver.find_element(By.XPATH, '//span[text()="7"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="+"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="8"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="="]').click()

    @allure.step(
            "Ждать 45 секунд, пока не появится "
            "результат сложения на табло калькулятора")
    def wait_result(self) -> str:
        """
        Ждет введенное ранее количество минут
        и выводит результат сложения на экран калькулятора
        """
        wait = WebDriverWait(self._driver, 45)
        wait.until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, ".screen"), "15"))

        screen = self._driver.find_element(By.CSS_SELECTOR, '.screen')

        return screen.text
