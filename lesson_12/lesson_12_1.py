mult = lambda a, b: a * b
# def mult(a, b):
#     return a * b
print(type(mult))

print(mult(3, 4))

lst_1 = ['Красноярск', 'Курск', 'Елец']

sorted_lst = sorted(lst_1, key=lambda word: len(word))

print(sorted_lst)


func = lambda x: x + 5
print(func(4))