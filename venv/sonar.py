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
