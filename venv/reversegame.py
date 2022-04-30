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
    return x >= 0 and x <= WIDTH -1 and y >= 0 and y <= HEIGHT -1

def getBoardWithValidMoves(board, tile):
    #  вернуть новое поле с точками, обозначающими допустимые ходы, которые может сделать игрок
    boardCopy = getBoardCopy(Copy)
