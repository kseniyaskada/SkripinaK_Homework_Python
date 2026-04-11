import allure
from selenium.webdriver.common.by import By


class CartPage:

    def __init__(self, driver):
        self._driver = driver

    @allure.step("Перейти на страницу 'Корзина'")
    def get_cart(self) -> None:
        """
        Переход на страницу корзины
        """
        self._driver.get("https://www.saucedemo.com/cart.html")

    @allure.step("Кликнуть на кнопку 'Checkout'")
    def checkout_button(self) -> None:
        """
        Нажатие кнопки 'Checkout'
        """
        self._driver.find_element(By.CSS_SELECTOR, '#checkout').click()
