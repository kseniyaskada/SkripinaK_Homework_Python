def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False


test_year = 2057
result = is_year_leap(test_year)

print("год " + str(test_year) + ": " + str(result))
