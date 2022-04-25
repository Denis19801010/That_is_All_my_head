# Шифр Цезаря
SYMBOLS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
MAX_KEY_SIZE = len(SYMBOLS)

def getMode():
    while True:
        print('Вы хотите зашифровать или расшифровать текст?')
        mode = input().lower()
        if mode in ['зашифровать', 'з', 'расшифровать', 'p']:
            return mode
        else:
            print('Введите"зашифровать"или"з"для зашифровки"или"расшифровать"или"р"для расшифровки.')

def getMessage():
    print('Введите текст:')
    return input()

def getKey():
    key = 0
    while True:
        print('Введите ключ шифрования (1-%s)' % (MAX_KEY_SIZE))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key

def getTranslatedMessage(made, message, key):
    if mode[0] =='р':
        key = -key
    translated = ''

    for sybol in message:


