# def example(*args):
#     *a, b = args
#     print(a, b)
#
#
# example(3, 56, 7, "ewfwe")
#
#
# def example(**kwargs):
#     print(kwargs)
#
#
# example(name="Даниил", age='35')

def print_name_age(name, age):
    print(f'Мое имя - {name} и мой возраст - {age}')

dict_1 = dict(name="Даниил", age='35')
dict_2 = {2: 44, 43: '34'}
print(dict_1)
print_name_age(**dict_1)

print({**dict_1, **dict_2})

a, *b = dict_1