# dict_ex = ["Даниил", "Николаев", "35", ["Москва", "Северодвинск", "Челябинск"]]
dict_ex = {"name": "Даниил", "last_name": "Николаев", "age": 35, "age": 37, "cities": ["Москва", "Северодвинск", "Челябинск"], "smoke": False}
#
# print(dict_ex['age'])

# dict_ex = dict(name="Даниил", last_name="Николаев")
# print(dict_ex)

# dict_ex = [["name", "Даниил"], ["last_name", "Николаев"]]
# print(dict(dict_ex))

# dict_ex = dict()

# """
# Ключами могут быть
# str
# int
# bool
# tuple
# """
# # del dict_ex['dqwfq']
#
# print(dict_ex)
# print('nam3e' in dict_ex)

# dict_ex = dict.fromkeys(["Даниил", "Николаев", "35"], "йцкк")
# dict_ex.clear()
# dict_ex_2 = dict_ex.copy()
# dict_ex_2 = dict(dict_ex)
# # dict_ex_2['name'] = "Даня"
# # dict_ex_2['ыацумауц'] = "ацуац"
# print(id(dict_ex))
# print(dict_ex)
# print(id(dict_ex_2))
# print(dict_ex_2)

# name = dict_ex.get("wqfqwfw", "Дмитрий")
# if name:
#     print(name)

# dict_ex.setdefault('efwefwefwe', "Дмитрий")
# print(dict_ex)
# print(dict_ex)
# str1 = dict_ex.pop('feqfqefq', "ключа нет")
# print(str1)
#
# print(dict_ex)

# print(dict_ex)
# item = dict_ex.popitem()
# print(item)
# item = dict_ex.popitem()
#
# print(dict_ex)

# print(list(dict_ex.keys()))
# print(list(dict_ex.values()))
# print(list(dict_ex.items()))

# for key, value in dict_ex.items():
#     print(key, value)

dict_ex1 = {"name": "Даниил"}
dict_ex2 = {"last_name": "Николаев"}

dict_ex1.update(dict_ex2)

print(dict_ex1)
print(dict_ex2)

dict_res = {**dict_ex1, **dict_ex2}

print(dict_res)

