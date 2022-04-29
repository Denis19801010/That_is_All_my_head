import random
import time


def displayIntro():
    print()
    print('''        Вы находитесь в землях заселёнными драконами
        Перед собой вы видите две пещеры. В одной пещере добрый дракон живёт, 
        который готов поделиться с вами своим богатством. В другой злой драконище, 
        который готов сожрать вас вместе с ботинками и труханами. ''')
    print()


def chooseCave():
    cave = ' '
    while cave != '1' and cave != '2': # будет проверять пока точно не введётся 1 или 2
        print('В какую пещеру ты хочешь войти? (нажми 1 или 2)')
        cave = input()

    return cave


def checkCave(chosenCave):
    print('Вы приближаетесь к пещере.....')
    time.sleep(4)
    print()
    print('Её темнота заставляет вас дрожать от страха.....')
    time.sleep(4)
    print()
    print('слегка попукивая от неизвестного вы продвигаетесь дальше....')
    time.sleep(4)
    print()
    print('шаг...пук...шаг...пук...шаг...пук...шaaaaaaаг........пуууууук...')
    time.sleep(4)
    print()
    print('БОЛЬШОЙ дракон выпрыгивает перед вами...раскрывает свою пасть иии.....')
    print()
    time.sleep(3)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('Делится своими сокровищами, да да просто так на халяву')

    else:
        print('Съедает вас нахрен всего')
        time.sleep(6)


playAgain = 'да'   # отсюда собственно и начинается наша программа
while playAgain == 'да':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)
    print('попытаешь ещё раз удачу? да или нет?')
    playAgain = input()
