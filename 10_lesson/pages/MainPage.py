import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:

    def __init__(self, driver):
        self._driver = driver

    @allure.step("Добавить в корзину 3 товара на странице")
    def add_products(self) -> None:
        """
        Добавляет товары в корзину
        """
        wait = WebDriverWait(self._driver, 10)
        wait.until(EC.url_contains('inventory'))

        self._driver.find_element(
            By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()

        self._driver.find_element(
            By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()

        self._driver.find_element(
            By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()
