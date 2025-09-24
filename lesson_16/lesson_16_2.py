"""
map(func, iterable)
"""

# numbers = ["1", '2', '3', '4']
#
# result = map(int, numbers)
# print(type(result))
# print(result)
# # print(list(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
#
# cities = ["Краснодар", 'Челябинск', 'Северодвинск', 'Златоуст']
#
# reverse = map(lambda str_1: str_1[::-1], cities)
# print(list(reverse))

"""
filter(func, iterable)
"""
# numbers = [2, 3, 4, 5]
# def dasd(x):
#     return True
#
# even_nums = filter(lambda x: x % 2 == 0, numbers)
# # print(list(even_nums))
# print(next(even_nums))
# print(next(even_nums))
# print(next(even_nums))
"""
zip(iterable1, iterable2, iterable3, ...)
"""

# a = ['dsadas', 33, 434, 'sdf']
# b = ['fdsfsd', 111, 555, 'f;ioliosdfsdf', 'wfqwfq']
# c = ['qwdq', 999, 90, 'qqqqq']

a = ['dsadas', 33, 434, 'sdf']
b = ('fdsfsd', 111, 555, 'f;ioliosdfsdf', 'wfqwfq')
c = 'dwqdwqdqwd'
# z_1, *z_2 = zip(a, b, c)
# print(z_1)
# print(list(z_2))

z = list(zip(a, b, c))

print(z)

z1, z2, z3 = zip(*z)
print(z1)
print(z2)
print(z3)
