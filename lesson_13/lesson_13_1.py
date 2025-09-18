# def decor(func):
#     def wrapper(*args, **kwargs):
#         print("До выполнения функции")
#
#         print("args", args)
#         print("kwargs", kwargs)
#         func(*args, **kwargs)
#         print("После выполнения функции")
#     return wrapper
#
# @decor
# def print_text(text):
#     print(f"простой текст {text}")
#
# print_text(text="Дополнительный текст")


# decor_print_text = decor(print_text)
#
# decor_print_text()

import time


def count_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Время выполнения: {end_time - start_time} сек")
        return result
    return wrapper

@count_time
def func_1():
    time.sleep(3)
    print('Фунция отработала')
    return "Возврат из функции"

# res = (func_1())
# print(res)

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Функция: {func.__name__}\nНеименнованные аргументы: {args}\nИменнованные аргументы: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Результат функции: {result}")
        return result
    return wrapper

@count_time
@logger
def summ(a, b):
    return a + b

res = summ(3, b=5)
