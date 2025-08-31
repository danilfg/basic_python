name = "Даниил"
age = "35"

text = f"Мое имя: {name}. Мой возраст: {age}"
# print(text)
#
text2 = "Мое имя: {0}. Мой возраст: {1}".format(name, age)
# print(text2)

text3 = "Мое имя: {imya}. Мой возраст: {vozrast}".format(vozrast=age, imya=name)
print(text3)