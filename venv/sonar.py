# охотник за сокровищами

import random
import sys
import math

def getNewBoard():
    # создать структуру данных( типо список в списке) нового игрового поля размером 60х15.
    board = []
    for x in range(60): # Главный список из 60 списков
        board.append([])
        for y in range(15): # Каждый список в главном списке содержит 15 односимвольных строк
            # Для создания океана используем разные символы, что бы сделать его реалистичнее
            if random.randint(0, 1) == 0:
                    board[x].append('~')
            else:
                    board[x].append('`')
    return board

def drawBoard(board):
    # изобразить структуру данных игрового поля
    tensDigitsLine = ' ' # создать место для чисел вниз по левой стороне поля
    for i in range(1, 6):
        tensDigitsLine += (' ' * 9) + str(i)

        # вывести числа в верхней части поля
        print(tensDigitsLine)
        print(' ' + ('0123456789' * 6))
        print()

        # вывести каждый из 15 рядов
        for row in range(15):
            # к однозначным числам нужно добавить дополнительный пробел
            if row < 10:
                extraSpace = ' '
            else:
                extraSpace = ''

            # создать строку для этого ряда на игровом поле
            boardRow = ''
            for column in range(60):
                boardRow += board[column][row]

            print('%s%s %s %s' % (extraSpace, row, boardRow, row))

    # вывести числа в нижней части поля
    print()
    print(' ' + ('0123456789' * 6))
    print(tensDigitsLine)

def getRandomChests(numChests):
    # создать список структур данных сундука(двухэлементные списки целочисленных координат x и y)
    chests = []
    while len(chests) < numChests:
        newChest = [random.randint(0, 59), random.randint(0, 14)]
    if newChest not in chests: # убедиться что сундука здесь еще нет
            chests.append(newChest)
    return chests
def isOnBoard(x, y):
    #  возвращать True если координаты есть на поле; в противном случае возвращать False
    return x >= 0 and x <= 59 and y >= 0 and y <= 14

def makeMove(board, chests, x, y):
    #  изменить структуру данных поля, используя символ гидролокатора. Удалить сундуки с сокровищами из списка
    #  с сундуками, как только их нашли. Вернуть False, если это недопустимый ход.  В противном случае вернуть строку
    #  с результатом этого хода.

    smallestDistance = 100  # все сундуки будут расположены ближе, на расстоянии в 100 едениц
    for cx, cy in chests:
        distance = math.sqrt((cx - x) * (cx - x) + (cy - y) * (cy - y))

        if distance < smallestDistance: # нам нужен ближайший сундук с сокровищами
            smallestDistance = distance

    smallestDistance = round(smallestDistance)

    if smallestDistance == 0:
    #  координаты xy попали прямо в сундук с сокровищами
        chests.remove([x, y])
        return 'Вы нашли сундук с сокровищами на дне океана!'
    else: