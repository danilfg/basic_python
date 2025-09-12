"""
set
"""

# set_1 = {1, 2, 4, 5, True, "str", (9, 5)}
# print(set_1)
# print(type(set_1))

"""
Изменяемые типы данных
list
dict
set

Неизменные типы данных
int
float
str
tuple
bool
"""

# set_2 = {[1,2], {2, 3}}

# set_3 = {} # здесь создастся словарь а не множество
# set_4 = set()
#
# print(type(set_3))
# print(type(set_4))

lst = [1, 2, 4, 5, 6, 6,  (1, 2), (1, 2)]
# print(set(lst))
#
# str_1 = "qweqweqwe"
# print(set(str_1))
#
# range_1 = range(5)
# print(set(range_1))

set_5 = set(lst)
# print(len(set_5))
# print((1,) in set_5)
# for item in set_5:
#     print(item)
# it = iter(set_5)
# print(next(it))

# set_5.add('234124')
#
# set_5.update(['324', '232', 'dasf'])
#
# set_5.update('vjnwvnwejk')
# print(set_5)
#
# # set_5.discard('234124wdwdw')
# # set_5.remove('234124sdasd')
# set_5.clear()
# print(set_5)

set_6 = {1, 2, 3, 4, 5}
set_7 = {4, 5, 6, 7, 8}
set_8 = {9, 10}

# res = set_6 & set_7
# res = set_6.intersection(set_7)
# set_6 &= set_7
# res = set_6 & set_8

# res = set_6 | set_7
# res = set_6.union(set_7)
# set_6 |= set_7

# res = set_7 - set_6
# res = set_6.difference(set_7)
# set_6 -= set_7

# res = set_6 ^ set_7
# res = set_6.symmetric_difference(set_7)
# set_6 ^= set_7

print(set_6 != set_7)

