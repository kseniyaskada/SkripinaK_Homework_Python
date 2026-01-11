import math


def square(side):
    return math.ceil(side*side)


print(square(9))

# второй вариант решения с возведением в степень:


def square(side):
    return math.ceil(side**2)


print(square(10.1))
