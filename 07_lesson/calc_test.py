from selenium import webdriver
from pages.CalcPage import CalcPage


def test_calculator():

    browser = webdriver.Chrome()

    calc_page = CalcPage(browser)
    calc_page.delay_field_input()
    calc_page.click_buttons()
    as_is = calc_page.wait_result()

    assert as_is == '15'

    browser.quit()
