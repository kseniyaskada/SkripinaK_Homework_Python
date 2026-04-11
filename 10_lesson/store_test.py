import allure
from selenium import webdriver
from pages.MainPage import MainPage
from pages.AuthPage import AuthPage
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage


@allure.title("Тест онлайн-магазина")
@allure.description(
    "Проверка добавление товара в корзину, оформление заказа и итоговой суммы")
@allure.feature("ORDER")
@allure.severity("MAJOR")
def test_store():

    browser = webdriver.Firefox()

    auth_page = AuthPage(browser)
    auth_page.authorization("standard_user", "secret_sauce")
    MainPage(browser).add_products()
    cart_page = CartPage(browser)
    cart_page.get_cart()
    cart_page.checkout_button()
    checkout = CheckoutPage(browser)
    checkout.input_info("Иван", "Иванов", "111000")
    as_is = checkout.find_price()

    with allure.step("Закрыть драйвер"):
        browser.quit()

    with allure.step("Проверить, что результат = 58.29"):
        assert as_is == 58.29
