def bacon():
    spam = 99  # создаёт локальную переменную с именем spam
    print(spam)  # выводит 99


spam = 42  # coздает глобальную переменную
print(spam)  # выводит 42
bacon()  # Вызывает функцию bacon
print(spam)  # выводит 42


def sayHello(name):
    print('Привет, ' + name + '. Твоё имя состоит из ' + str(len(name)) + ' ,букв. ')


sayHello('Alice')
sayHello('Vasily')
spamer = 'Katy'
sayHello(spamer)

