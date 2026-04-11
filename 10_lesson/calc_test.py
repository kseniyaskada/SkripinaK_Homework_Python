import allure
from selenium import webdriver
from pages.CalcPage import CalcPage


@allure.title("Тест калькулятора")
@allure.description(
    "Проверка работы оджидания калькулятора "
    "и сравнение итогового результата с ожидаемым")
@allure.feature("WAIT")
@allure.severity("MAJOR")
def test_calculator():

    browser = webdriver.Chrome()

    calc_page = CalcPage(browser)
    calc_page.delay_field_input()
    calc_page.click_buttons()
    as_is = calc_page.wait_result()

    with allure.step("Проверить, что результат = 15"):
        assert as_is == '15'

    with allure.step("Закрыть драйвер"):
        browser.quit()
