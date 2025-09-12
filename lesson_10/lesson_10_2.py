# set_1 = {x ** 2 for x in range(1, 5)}
# print(set_1)

# lst_1 = [1, 2, 4, '6', -2, '43', '4']
# set_2 = {int(x) for x in lst_1}
# set_3 = {int(x) for x in lst_1 if int(x) > 5}
# print(set_3)

# dict_1 = {x: x ** 2 for x in range(1, 5)}
# print(dict_1)

dict_2 = {'Россия': "москва", "Франция": "париж", "США": "вашингтон"}
dict_3 = {key.upper(): value.capitalize() for key, value in dict_2.items()}
print(dict_2)
print(dict_3)
