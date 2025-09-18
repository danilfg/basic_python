from functools import wraps


def logger(print_res=True):
    def logger_inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Функция: {func.__name__}\nНеименнованные аргументы: {args}\nИменнованные аргументы: {kwargs}")
            result = func(*args, **kwargs)
            if print_res:
                print(f"Результат функции: {result}")
            return result
        return wrapper
    return logger_inner

@logger(False)
def summ(a, b):
    return a + b

print(summ.__name__)
res = summ(3, b=5)