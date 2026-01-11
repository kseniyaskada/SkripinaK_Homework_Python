def month_to_season(month):
    if 1 <= month <= 2:
        print("Зима")
    if 3 <= month <= 5:
        print("Весна")
    if 6 <= month <= 8:
        print("Лето")
    if 9 <= month <= 11:
        print("Осень")
    if month == 12:
        print("Зима")


month_to_season(6)
