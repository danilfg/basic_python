"""
DRY - Don't Repeat Yourself


iter()
str()
list()
print()
"""

# func = print
# func("Вывод в консоль")
# print = "Это строка"
# func(id(print))
# func(id(func))

def print_text(add_text):
    text = f"текст для печати: {add_text}"
    print("add_text", id(add_text))
    print(text)


str_1 = "Курс от Даниила"
int_1 = 1212
# print("str_1", id(int_1))
# print_text(int_1)

iter_1 = iter(str_1)

def summarize_two(x, y):
    res_sum = x + y
    return res_sum

def multply_two(x, y):
    res_mult = x * y
    return res_mult

def common(x, y):
    return summarize_two(x, y), multply_two(x, y)


# print(common(4, 5))
# res = summarize_two(1, 2)
# print(res)
#
# sum_1, mult_1 = summarize_two(1, 2)
# print(sum_1)
# print(mult_1)

def is_negative(x):
    return x < 0

# print(is_negative(0))
# print(is_negative(1))
# print(is_negative(-1))

lst = [1, -4, 4, -133, 0, 23, -24]

for item in lst:
    if is_negative(item):
        print(item, end=" ")