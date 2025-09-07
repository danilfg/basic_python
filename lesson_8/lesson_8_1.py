"""
Итерируемые объекты
строки (str)
списки (list)
кортежи (tuple)
диапозоны чисел (range)
словари (dict)
множества (set)
"""
from time import sleep

numbers = [34, 63, 53, 93, 1, 0, 31]
it_numbers = iter(numbers)
# print(type(it_numbers))
# print(next(it_numbers))
# print(next(it_numbers))
# print(next(it_numbers))
# print(next(it_numbers))
# print(next(it_numbers))
# print(next(it_numbers))
# print(next(it_numbers))
# print(next(numbers))

str_1 = "Даниил"
it_str_1 = iter(str_1)
# print(type(it_str_1))
# print(next(it_str_1))
# print(next(it_str_1))
# print(next(it_str_1))
# print(next(it_str_1))
# sleep(4)
# print(next(it_str_1))
# print(str_1[0])

for letter in str_1:
    print(letter)