# def get_num(x, y, z=5):
#     print("x =", x)
#     print("y =", y)
#     print("z =", z)

x_1 = 1
y_1 = 2
z_1 = 3
#
# get_num(x_1, y_1, z_1)
# get_num(x_1, y_1, z_1)
#
# get_num(3, 4, 2)

# def get_lower_or_upper_str(str1, lower=True, upper=False):
#     if lower:
#         return str1.lower()
#     elif upper:
#         return str1.upper()
#     else:
#         return str1
#
# print(get_lower_or_upper_str('Даниил'))
# print(get_lower_or_upper_str('Даниил', lower=False))
# print(get_lower_or_upper_str('Даниил', lower=False, upper=True))


def add_value(value, lst=None):
    if not lst:
        lst = []
    lst.append(value)
    return lst

print(add_value(1))
print(add_value(4, []))
print(add_value(2))
