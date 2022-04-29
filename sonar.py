# охотник за сокровищами

import random
import sys
import math

def getNewBoard():
    # создать структуру данных( типо список в списке) нового игрового поля размером 60х15.
    board = []
    for x in range(60):  # Главный список из 60 списков
        board.append([])
        for y in range(15):  # Каждый список в главном списке содержит 15 односимвольных строк
            # Для создания океана используем разные символы, что бы сделать его реалистичнее
            if random.randint(0, 1) == 0:
                board[x].append('~')
            else:
                board[x].append('`')
    return board

def drawBoard(board):
    # изобразить структуру данных игрового поля
    tensDigitsLine = '  '  # создать место для чисел вниз по левой стороне поля
    for i in range(1, 6):
        tensDigitsLine += (' ' * 9) + str(i)

        # вывести числа в верхней части поля
        print(tensDigitsLine)
        print('   ' + ('0123456789' * 6))
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
    print('  ' + ('0123456789' * 6))
    print(tensDigitsLine)

def getRandomChests(numChests):
# создать список структур данных сундука(двухэлементные списки целочисленных координат x и y)( добавляет три сундука)
    chests = []
    while len(chests) < numChests:
        newChest = [random.randint(0, 59), random.randint(0, 14)]
        if newChest not in chests:  # убедиться что сундука здесь еще нет
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

        if distance < smallestDistance:  # нам нужен ближайший сундук с сокровищами
            smallestDistance = distance

    smallestDistance = round(smallestDistance)

    if smallestDistance == 0:
        #  координаты xy попали прямо в сундук с сокровищами
        chests.remove([x, y])
        return 'Вы нашли сундук с сокровищами на дне океана!'
    else:
        if smallestDistance < 10:
            board[x][y] = str(smallestDistance)
            return 'Сундук с сокровищами обнаружен на расстоянии %s от гидролокатора' % (smallestDistance)
        else:
            board[x][y] = 'X'
            return 'Гидролокатор ничего не обнаружил. Все сундуки с сокровищами вне пределов досягаемости'

def enterPlayerMove(previousMoves):
    #  позволить игроку сделать ход. Вернуть двухэлементный список с целыми координатами x и y.
    print('Где следует опустить гидролокатор? (координаты: 0-59, 0-14) (или введите "выход")')
    while True:
        move = input()
        if move.lower() == 'выход':
            print('Спасибо за игру, удачи в гачи!')
            sys.exit()

        move = move.split()
        if len(move) == 2 and move[0].isdigit() and move[1].isdigit() and isOnBoard(int(move[0]), int(move[1])):
            if [int(move[0]), int(move[1])] in previousMoves:
                print('В этом месте уже всё обыскали!')
                continue
            return [int(move[0]), int(move[1])]

        print('Введи число от 0 до 59, потом пробел, а затем число от 0 до 14.')


def showInstructions():
    print('''Вы - капитан корабля, плывущего за сокровищами. Ваша задача - с помощью гидролокаторов найти три 
    сундука с сокровищами в затонувших кораблях на дне океана. Но Гидролокаторы очень просты и определяют только 
    расстояние, но не направление. Введите координаты, чтобы опустить гидролокатор в воду. На карте будет показано
    число, обозначающее на каком расстоянии находится ближайший сундук. Или будет показана буква Х, обозначающая, что 
    сундук в области действия гидролокатора не обнаружен. На карте метки С - это сундуки. Цифра 3 обозначает, что 
    ближайший сундук находится на отдалении в 3 еденицы.
    
                                             1         2         3
                                   012345678901234567890123456789012
                                   
                                   0````~~~~``~`~`````~~~~~~~````~~~~0
                                   1~``~~~~``~~``~``~`````~~``~~~~``~1
                                   2~~~C~~3``````C~~~~`~~~~~~~````~~`2
                                   3~~~~~~~~~``````~~~``~~~``~~``~~`~3
                                   4`~~~~~~~~~```C~~`~~``~`~~~~~~``~~4
                                            
                                   012345678901234567890123456789012
                                             1         2         3
                                             
                                             
                                        
    (во время игры сундуки на карте не обозначаются!)
    
    Нажми клавишу  Enter чтобы продолжить...''')
    input()

    print(''' Если гидролокатор опущен прямо на сундук, вы сможете поднять сундук. Другие гидролокаторы обновят данные
    о расположении ближайшего сундука. Сундуки ниже находятся вне диапазона локатора, поэтому отображается буква Х 
    
                                             
                                             1         2         3
                                   012345678901234567890123456789012
                                   
                                   0````~~~~``~`~`````~~~~~~~````~~~~0
                                   1~``~~~~``~~``~``~`````~~``~~~~``~1
                                   2~~~Х~~7``````C~~~~`~~~~~~~````~~`2
                                   3~~~~~~~~~``````~~~``~~~``~~``~~`~3
                                   4`~~~~~~~~~```C~~`~~``~`~~~~~~``~~4
                                            
                                   012345678901234567890123456789012
                                             1         2         3
    
    Сундуки не перемещеются. Гидролокаторы определяют сундуки на расстоянии до 9 едениц. Попробуйте поднять 
    все три сундука до того как все гидролокаторы будут опущены на дно. Good Luck!
    
    
    Нажмите кнопку Enter, чтобы продолжить...''')
    input()


print('О Х О Т Н И К   З А    С О К Р О В И Щ А М И!')
print()
print('Показать инструктаж? (да/нет)')
if input().lower().startswith('д'):
    showInstructions()

while True:
    #  настройка игры
    sonarDevices = 80
    theBoard = getNewBoard()
    theChests = getRandomChests(100)
    drawBoard(theBoard)
    previousMoves = []

    while sonarDevices > 0:
        # показать гидролокаторные устройства и сундуки с сокровищами.
        print('Осталось гидролокаторов: %s. Осталось сундуков с сокровищами: %s' % (sonarDevices, len(theChests)))

        x, y = enterPlayerMove(previousMoves)
        previousMoves.append([x, y])  # мы должны отслеживать все ходы, что бы гидролокаторы могли обновляться.

        moveResult = makeMove(theBoard, theChests, x, y)
        if moveResult == False:
            continue
        else:
            if moveResult == 'Вы нашли сундук с сокровищами на затонувшем корабле!':
                # обновить все гидролокационные устройства, в настоящее время нходящиеся на карте.
                for x, y in previousMoves:
                    makeMove(theBoard, theChests, x, y)
            drawBoard(theBoard)
            print(moveResult)

        if len(theChests) == 0:
            print('Вы нашли все сундуки с сокровищами на затонувших судах! Поздравляем и хватит фигнёй заниматься'
                  'иди работай')
            break
        sonarDevices -= 1

    if sonarDevices == 0:
        print('Все гидролокаторы закончились, придется разворачивать корабли и валить за новыми')
        print('ГАМЕОВЕР!')
        print('Ты не нашел сундуки, а они были тут и там:')
        for x, y in theChests:
            print('   %s, %s' % (x, y))
    print('Хочется ещё разик сыграть?(да или нет?')
    if not input().lower().startswith('д'):
        sys.exit()