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


