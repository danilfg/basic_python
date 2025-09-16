# name = 'Даниил' # Глобальная переменная
#
# def func():
#     def func_2():
#         name = 'Д'
#         print(name)
#     name = 'ДАНИИЛ' # Локальная  переменная
#     print(name)
#
# func()
# print(name)
# print(name)

"""
Очередность поиска переменных
Local - локальная переменная (внутри функицц)
Global - глобальная переменная (вне функции)
Builtin - встроенная в пайтон (print, str и т.п.)
"""

# NAME = 'Даниил'

def update_name():
    NAME = 'Даниил'
    def update_name_2():
        nonlocal NAME
        NAME = 'Михаил'
        print('update_name_2', NAME)

    update_name_2()
    print('update_name', NAME)

update_name()
# print(NAME)
