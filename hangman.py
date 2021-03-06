import random
HANGMAN_PICS = [''' 
  +---+
      |
      |
      |
     ===''', '''
  +---+
      |
       |
       |
      ===''', '''
  +---+
  0   |
  |   |
      |
     ===''', '''
  +---+
  0   |
 /|   |
      |
     ===''', '''
  +---+
  0   |
 /|\  |
      |
     ===''', '''
  +---+
  0   |
 /|\  |
 /    |
     ===''', '''
  +---+
  0   |
 /|\  |
 / \  |
     ===''']
word = 'аист акула бабуин барсук бобр баран бык верблюд волк воробей ворон выдра голубь гусь жаба зебра змея индюк'\
    'кит кобра коза козел койот корова кошка кролик крыса курица лампа ласка лебедь лев лиса лосось лось лягушка'\
    'медведь моллюск моль мул муравей мышь норка носорог обезьяна овца окунь олень орел осел панда паук питон попугай'\
    'пума семга скунс собака сова тигр тритон тюлень утка форель хорек черепаха ястреб ящерица'. split()

def getRandomWord(wordList):    #  эта функция возвращает случайную строку из переданного списка(создает секретное слово)
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):  # отображение игрового поля
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Ошибочные буквы: ', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): # заменяет пропуски отгаданными буквами
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]

    for letter in blanks :  # Показывает секретное слово с пробелами между буквами
        print(letter, end= ' ')
    print()

def getGuess(alreadyGuessed): # возвращает букву, введенную игроком. Эта функция проверяет, что игрок ввёл только одну букву и ничего больше
    while True:
        print('Введите букву. ')
        guess = input()
        guess = guess.lower()    # Если игрок ввёл большие( ПРОПИСНЫЕ) буквы, тут они понижаются до строчных
        # Проверка допустимости предположения игрока
        if len(guess) != 1:      # Проверка что введена одна буква
            print('пожалуйста, введите одну букву.')
        elif guess in alreadyGuessed:   # Проверка что буква не была угадана ранее
            print('Вы уже выбирали эту букву. Назови другую')
        elif guess not in 'абвгдеежзиклмнопрстуфхцчшщъыьэюя':  # проверяет, что введен символ стандартного русского алфавита
            print('Пожалуйста введите БУКВУ!')
        else:
            return guess   # если условия не выполняются то цикл начинается сначала

def playAgain(): # эта функция возвращает значение True, если игрок хочет сыграть заново; В противном случае False.
    print('Хотите сыграть еще? (да или нет)' )
    return input().lower().startswith('д')  # начинаем сначала игру если да

# Начинается основная часть (тело) программы. Все, что выше этой строки, «всего лишь» описание функций
print(' В И С Е Л И Ц А ')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(word)
gameIsDone = False

while True: # вызываем функцию displayBoard передаем её значения трех переменных( mis, corr, sec)
    displayBoard(missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters) # позволяет игроку ввести угадываемую букву

    if guess in secretWord:
        correctLetters = correctLetters + guess # проверяет выиграл ли игрок
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Да! Секретное слово - "' + secretWord + '"!  Вы угадали!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess # проверяет превысил ли игрок лимит попыток и проиграл.
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('Вы исчерпали все попытки!\nНеугадано букв: ' + str(len(missedLetters)) + ' и угадано букв: '  + str(len(correctLetters)) + '. Было загадано слово "' + secretWord + '".')
            gameIsDone = True #  запрашивает хочет ли игрок сыграть заново( только если игра закончена).
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(word)
        else:
            break