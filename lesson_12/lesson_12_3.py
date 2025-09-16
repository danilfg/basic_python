def say_name(name):
    def say_goodbye():
        print(f"Пока, {name}")

    return say_goodbye

say_daniil = say_name('Даниил')
say_igor = say_name('Игорь')

say_daniil()
say_igor()

def printsdsa():
    print(1243)
print(say_daniil.__closure__)
print(printsdsa.__closure__)
