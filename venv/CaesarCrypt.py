# Шифр Цезаря
SYMBOLS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
MAX_KEY_SIZE = len(SYMBOLS)


def getMode():
    while True:
        print('Вы хотите зашифровать или расшифровать текст?')
        mode = input().lower()
        if mode in ['зашифровать', 'з', 'расшифровать', 'р']:
            return mode
        else:
            print('Введите"зашифровать"или"з"для зашифровки"или"расшифровать"или"р"для расшифровки.')


def getMessage():   # просто получает сообщения для шифрования или расшифровки и возвращает его
    print('Введите текст:')
    return input()


def getKey():
    # позволяет ввести ключ, который будет использоваться для шифровки расшифровки сообщения
    key = 0
    while True:
        print('Введите ключ шифрования (1-%s)' % (MAX_KEY_SIZE))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key


def getTranslatedMessage(mode, message, key):
    # выполнение расшифровки/шифровки сообщения
    # mode.Этот параметр устанавливает функцию в режим шифрования или расшифровывания
    # message.Это открытый текст(или шифротекст), который должен быть зашифрован(или расшифрован);
    # key.Это ключ, который используется в  этом шифре.
    if mode[0] == 'р':
        key = -key
    translated = ''

    for symbol in message:
        symbolIndex = SYMBOLS.find(symbol)
        if symbolIndex == -1:  # Символ не найден в SYMBOLS
            #  просто добавить этот символ без изменений
            translated += symbol
        else:
            #  зашифровать или расшифровать
            symbolIndex += key

            if symbolIndex >= len(SYMBOLS):
                symbolIndex -= len(SYMBOLS)
            elif symbolIndex < 0:
                symbolIndex += len(SYMBOLS)

            translated += SYMBOLS[symbolIndex]
    return translated
# запушил

mode = getMode()
message = getMessage()
key = getKey()
print('Преобразованный текст: ')
print(getTranslatedMessage(mode, message, key))
