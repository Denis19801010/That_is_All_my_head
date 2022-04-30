# "реверси": клон "Отелло"
import random
import sys

WIDTH = 8  # игровое поле содержит 8 клеток по ширине
HEIGHT = 8  # игровое поле содержит 8 клеток по высоте


def drawBoard(board):
    # вывести игровое поле, переданное этой функции. Ничего не возвращать
    print('  12345678')
    print(' +--------+')
    for y in range(HEIGHT):
        print('%s|' % (y + 1), end='')
        for x in range(WIDTH):
            print(board[x][y], end='')
        print('|%s' % (y + 1))
    print(' +--------+')
    print('  12345678')


def getNewBoard():
    # создать структуру данных нового чистого игрового поля
    board = []
    for i in range(WIDTH):
        board.append([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
    return board


def isValidMove(board, tile, xstart, ystart):
    # вернуть False, если ход игрока в клетку с координатами xstart, ystart недопустимый
    # если это допустимый ход, вернуть список клеток, которые присвоили бы игрок если бы сделал туда ход
    if board[xstart][ystart] != ' ' or not isOnBoard(xstart, ystart):
        return False
    if tile == 'X':
        otherTile = 'O'
    else:
        otherTile = 'X'

        tilesToFlip = []

    for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        x, y = xstart, ystart
        x += xdirection  # первый шаг в направлении x
        y += ydirection  # первый шаг в направлении y
        while isOnBoard(x, y) and board[x, y] == otherTile:
            #  продолжать двигаться в этом направлении  x и y
            x += xdirection
            y += ydirection
            if isOnBoard(x, y) and board[x][y] == tile:
                #  есть фишки которые можно перевернутью двигаться в обратном направлении до достижения исходной
                #  клетки, отмечая все фишки на этом пути
                while True:
                    x -= xdirection
                    y -= ydirection
                    if x == xstart and y == ystart:
                        break
                    tilesToFlip.append([x, y])
    if len(tilesToFlip) == 0:  # если ни одна из фишек не перевернулась это недопустимый ход
        return False
    return tilesToFlip


def isOnBoard(x, y):
    # вернуть True если координаты есть на игровом поле
    return x >= 0 and x <= WIDTH - 1 and y >= 0 and y <= HEIGHT - 1


def getBoardWithValidMoves(board, tile):
    #  вернуть новое поле с точками, обозначающими допустимые ходы, которые может сделать игрок
    boardCopy = getBoardCopy(board)

    for x, y in getValidMoves(boardCopy, tile):
        boardCopy[x][y] = '.'
        return boardCopy


def getValidMoves(board, tile):
    #  вернуть список списков с координатами х и у допустимых ходов для данноого игрока на данном игровом поле
    validMoves = []
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if isValidMove(board, tile, x, y) != False:
                validMoves.append([x, y])
    return validMoves


def getScoreOfBoard(board):
    #  определить количество очков, подсчитав фишки. Вернуть словарь с ключами 'Х' и 'О'
    xscore = 0
    oscore = 0
    for i in range(WIDTH):
        for y in range(HEIGHT):
            if board[x][y] == 'X':
                xscore += 1
            if board[x][y] == 'O':
                oscore += 1
    return {'X': xscore, 'O': oscore}


def enterPlayerTile():
    #  позволить игроку ввести выбранную фишку
    #  возвращает список с фишкой игрока в качестве первого элемента и фишкой компьютера в качестве второго
    tile = ''
    while not (tile == 'X' or tile == 'O'):
        print('вы играете за Х или О?')
        tile = input().upper()

    #  первый элемент в списке фишка игрока, второй элемент фишка компа
    if tile == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def whoGoesFirst():
    #  случайно выбрать кто ходит первым
    if random.randint(0, 1) == 0:
        return 'компик'
    else:
        return 'человек'


def makeMove(board, tile, xstart, ystart):
    #  поместить фишку на игровое поле в позицию xstart, ystart и перевернуть какую либо фишку противкина
    #  вернуть False если это недопустимый ход, вернуть если True допустимый
    tilesToFlip = isValidMove(board, tile, xstart, ystart)

    if tilesToFlip == False:
        return False

    board[xstart][ystart] = tile
    for x, y, in tilesToFlip:
        board[x][y] = tile
    return True


def getBoardCopy(board):
    #  сделать копию списка board и вернуть ee
    boardCopy = getNewBoard()

    for x in range(WIDTH):
        boardCopy[x][y] = board[x][y]

    return boardCopy


def isOnCorner(x, y):
    #  вернуть True если указанная позиция находиться в одном из 4-х углов
    return (x == 0 or y == WIDTH - 1) and (y == 0 or y == HEIGHT - 1)


def getPlayerMove(board, playerTile):
    #  позволить игроку ввести свой ход
    #  вернуть ход в виде [х, у] ( или вернуть строки 'подсказка' или 'выход')
    DIGITS1TO8 = '1 2 3 4 5 6 7 8'.split()
    while True:
        print('Укажите ход, текст "выход" для завершения игры или "подсказка" для получения подсказки')
        move = input().lower()
        if move == 'выход' or move == 'подсказка':
            return move

        if len(move) == 2 and move[0] in DIGITS1TO8 and move[1] in DIGITS1TO8:
            x = int(move[0]) - 1
            y = int(move[1]) - 1
            if isValidMove(board, playerTile, x, y) == False:
                continue
            else:
                break
        else:
            print('Это недопустимый ход. Введите номер столобца (1-8) и номер ряда (1-8)')
            print('К примеру значение 81 перемещает в верхний правый угол')

    return [x, y]


def getComputerMove(board, computerTile):
    #  учитывая данное игровое поле и данную фишку компьютера, определить,
    #  куда сделать ход, и вепнуть этот ход в виде списка[x, y]
    possibleMoves = getValidMoves(board, computerTile)
    random.shuffle(possibleMoves)  # сделать случайным порядок ходов

    #  всегда делать ход в угол, если это возможно
    for x, y in possibleMoves:
        if isOnCorner(x, y):
            return [x, y]

    #  найти ход с наибольшим количеством очков
    bestScore = -1
    for x, y in possibleMoves:
        boardCopy = getBoardCopy(board)
