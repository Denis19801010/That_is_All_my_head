# крестики-нолики

import random


def drawBoard(board):  # эта функция выводит на экран игровое поле, клетки которого будут заполняться
    print(board[7] + '|' + board[8] + '|' + board[9])
    # "board" -это список из 10 строк, для прорисовки игрового поля(индекс 0 игнорируется)
    print('-+-+-')
    print(board[4] + '|' + board[5] + "|" + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])


def inputPlayerLetter():  # разрешение игроку ввести букву, которую он выбирает
    letter = ''  # Возвращает список, в которм буква игрока -первый элемент, а ИИ -второй
    while not (letter == 'X' or letter == 'O'):
        print('Вы выбираете Х или О')
        letter = input().upper()

        # первым элементом списка является буква игрока, вторым - буква ИИ
        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']


def whoGoesFirst():  # случайный выбор игрока, который ходит первым.
    if random.randint(0, 1) == 0:
        return 'Компьютер'
    else:
        return 'Человек'


def makeMove(board, letter, move):
    board[move] = letter


def isWinner(bo,
             le):  # учитывая заполнение игрового поля и буквы игрока, эта функция возвращвет True если игрок выиграл
    # Мы используем "bo" вместо board и "le" вместо letter, что бы не печатать много
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # across the top
            (bo[4] == le and bo[5] == le and bo[6] == le) or  # через центр
            (bo[1] == le and bo[2] == le and bo[3] == le) or  # через низ
            (bo[7] == le and bo[4] == le and bo[1] == le) or  # вниз по левой стороне
            (bo[8] == le and bo[5] == le and bo[2] == le) or  # вниз по центру
            (bo[9] == le and bo[6] == le and bo[3] == le) or  # вниз по правой стороне
            (bo[7] == le and bo[5] == le and bo[3] == le) or  # по диагонали
            (bo[9] == le and bo[5] == le and bo[1] == le))  # по диагонали


def getBoardCopy(board):
    # создаёт копию игрового поля и возвращает его
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy


def isSpaceFree(board, move):
    # возвращает True, если сделан ход в свободную клетку
    return board[move] == ' '


def PlayerMove(board):
    # разрешение игроку сделать ход
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('Ваш следующий ход? (1-9)')
        move = input()
    return int(move)


def choseRandomMoveFromList(board, movesList):
    # возвращает допустимый ход, учитывая список сделанных ходов и список заполненных клеток
    # возвращает значение None, если больше нет допустимых ходов
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None


def getComputerMove(board, computerLetter):
    # учитывая заполнение игрового поля и букву компьютера,определяет допустимый ход и возвращает его
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'Х'

    # Это алгоритм для ИИ "Крестиков - ноликов"
    # Сначала проверим - победим ли мы, сделав следующий ход
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i

    # проверяем победит ли игрок, сделав следующий ход, и блокируем его
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i

    # пробуем занять один из углов, если есть свободные
    move = choseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    # пробуем занять центр если он свободен
    if isSpaceFree(board, 5):
        return 5

    # делаем ход по одной стороне
    return choseRandomMoveFromList(board, [2, 4, 6, 8])


def isBoardFull(board):
    # возвращает True, если клетка на игровом поле занята. В противном случае, возвращает False
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


print('Игра КРЕСТИКИ-НОЛИКИ')

while True:
    # перезагрузка игрового поля
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('' + turn + ' ходит первым.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'Человек':
            # Ход игрока
            drawBoard(theBoard)
            move = PlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Урааааа Вы ВЫИГРАЛИ!!!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('НИКТО НЕ ВЫИГРАЛ. НИЧЬЯ')
                    break
                else:
                    turn = 'Компьютер'

        else:
            # Ход компьютера
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('Тупая железка тебя победила. Ты продул')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('Ничья')
                    break
                else:
                    turn = 'Человек'

    print('Сыграем еще раз? (да или нет)')
    if not input().lower().startswith('д'):
        break
