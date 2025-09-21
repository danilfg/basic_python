file_1 = "lesson_15.txt"
file_2 = "../requirements.txt"
file_3 = "/Users/danilfg/repos/projects/basic_python/lesson_15/lesson_15.txt"
file_4 = "screen.png"
"""
r - read
w - write
a - append
x - create

r+ - чтение и запись - файл должен существовать
w+ - запись и чтение - создает или очищает и перезаписывет существующий
a+ - добавление и чтение - можем читать и записывать в конец файла
"""


# f = open(file=file_2)
# print(type(f))

# text_2 = f.read()
# print(type(text_2))
# print(text_2)
# text_2_line = f.readline()
# print(type(text_2_line))
# print(text_2_line)
#
# text_2_lines = f.readlines() # не использовать для больших файлов
# print(type(text_2_lines))
# print(text_2_lines)
#
# for line in f:
#     print(line, end='')

# print("Позиция до чтения", f.tell())
# text_2_line = f.readline()
# print("Позиция после чтения", f.tell())
# f.seek(0)
# print("Позиция после f.seek(0)", f.tell())
# f.seek(50)
# text_2 = f.read(10)
# print(text_2)
# text_2 = f.read(10)
# print(text_2)
# # print(type(text_2_line))
# # print(text_2_line)
# f.close()
# f = open(file_2)
file_5 = "screen.png"
with open(file_5, mode="rb") as f:
    image = f.read()

with open('screenshot_2.png', mode="wb") as f:
    f.write(image)

