"""
w - write
a - append

w+ - запись и чтение - создает или очищает и перезаписывет существующий
a+ - добавление и чтение - можем читать и записывать в конец файла
"""
#
# file_5 = "screen.png"
# with open(file_5, mode="rb") as f:
#     image = f.read()
#
# with open('screen_2.png', mode="wb") as f:
#     f.write(image)

# with open("out.txt", "w", encoding='utf-8') as f:
#     f.write('text1\n')
#     f.write('text3\n')
#
# with open("out.txt", "a", encoding='utf-8') as f:
#     f.write('text2\n')
#
# lst = ['dsafqwfwqfqw', 'qwfqwfqw']
# lst_for_w = [text + '\n' for text in lst]
#
# with open("out.txt", "a", encoding='utf-8') as f:
#     f.writelines(lst_for_w)

with open("out.txt", "a+") as f:
    print(f.tell())
    f.write('новая строка\n')
    f.seek(0)
    print(f.read())
