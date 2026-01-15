# дорогой наставник, я не смогла придумать негативный
# тест-кейс для метода contains (позитивные на строке 35), помоги, пожалуйста

import pytest
from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.positive_test
@pytest.mark.parametrize('input_txt, expected_output', [
    ('good day', 'Good day'),
    ('kseniya is my name', 'Kseniya is my name'),
    ('where is my key?', 'Where is my key?')
]
)
def test_string_utils_capitalize_positive(input_txt, expected_output):
    string_utils = StringUtils()
    res = string_utils.capitalize(input_txt)
    assert res == expected_output


@pytest.mark.positive_test
@pytest.mark.parametrize('input_txt, expected_output', [
    ("   Hi", "Hi"),
    ('   ', '')
]
)
def test_string_utils_trim_positive(input_txt, expected_output):
    string_utils = StringUtils()
    res = string_utils.trim(input_txt)
    assert res == expected_output


@pytest.mark.positive_test
@pytest.mark.parametrize('text, symbol, result', [
    ('Tacher', 'T', True),
    ('Homework', 'o', True),
    ('Good evening', 'k', False)
])
def test_string_utils_contains_positive(text, symbol, result):
    string_utils = StringUtils()
    res = string_utils.contains(text, symbol)
    assert res == result


@pytest.mark.positive_test
@pytest.mark.parametrize('text, symbol, result', [
    ('This is the bend', 'b', 'This is the end'),
    ('Hello, my name is John', 'h', 'Hello, my name is Jon'),
    ('Cool', 'o', 'Cl')
])
def test_string_utils_delete_symbol_positive(text, symbol, result):
    string_utils = StringUtils()
    res = string_utils.delete_symbol(text, symbol)
    assert res == result


@pytest.mark.negative_test
@pytest.mark.parametrize('input_txt, expected_output', [
    (' word', ' word'),
    ('5345room', '5345room'),
    ('', ''),
    (' ', ' ')
]
)
def test_string_utils_capitalize_negative(input_txt, expected_output):
    string_utils = StringUtils()
    res = string_utils.capitalize(input_txt)
    assert res == expected_output


@pytest.mark.negative_test
@pytest.mark.parametrize('input_txt, expected_output', [
    ("Word Hi", "Word Hi")
]
)
def test_string_utils_trim_negative(input_txt, expected_output):
    string_utils = StringUtils()
    res = string_utils.trim(input_txt)
    assert res == expected_output


@pytest.mark.negative_test
@pytest.mark.parametrize('text, symbol, result', [
    ('', '', ''),
    ('Hello', ' ', 'Hello'),
    ('Hello', '', 'Hello')
])
def test_string_utils_delete_symbol_negative(text, symbol, result):
    string_utils = StringUtils()
    res = string_utils.delete_symbol(text, symbol)
    assert res == result
