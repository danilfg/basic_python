"""
all()
any()
"""

lst = [True, True, False]
# print(all(lst))
# print(any(lst))

lst_1 = [1, 5, 'asda']
print(all(lst_1))
print(bool(0))
print(bool(''))

"""
bool возвращает False, если
0
''
[]
{}
"""

nums = [2, 1, 3, 4, 5, 6]
nums_bool = [x % 2 == 0 for x in nums]

print(nums)
print(nums_bool)

print(any(nums_bool))

if any(nums_bool):
    pass