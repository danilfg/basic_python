# numbers = [23, 43, 75, 33, 80, 51, 62]
# for number in numbers:
#     print("Печатаем:", number)

# for letter in "Даниил":
#     print('Буква:', letter)

# numbers = [23, 43, 75, 33, 80, 51, 62]
# for number in numbers:
#     number = 0
#
# print(numbers)

# range(start, stop, step)

# print(list(range(0, 10, 2)))

# numbers = [23, 43, 75, 33, 80, 51, 62]
# for i in range(len(numbers)):
#     numbers[i] = 0
#
# print(numbers)

words = ["Привет,", "Даниил!", "Как", "дела?"]

result_str = ''

for word in words:
    result_str += ' ' + word

print(result_str.lstrip())