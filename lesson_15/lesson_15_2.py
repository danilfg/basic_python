file_2 = "../requirements1.txt"

try:
    f = open(file_2)
    print("Файл открыт")
    try:
        text = f.read()
        print(text)
    finally:
        f.close()
        print("Файл закрыт")

except FileNotFoundError:
    print("Файл не найден")

