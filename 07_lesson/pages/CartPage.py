from selenium.webdriver.common.by import By


class CartPage:

    def __init__(self, driver):
        self._driver = driver

    def get_cart(self):
        self._driver.get("https://www.saucedemo.com/cart.html")

    def checkout_button(self):
        self._driver.find_element(By.CSS_SELECTOR, '#checkout').click()
