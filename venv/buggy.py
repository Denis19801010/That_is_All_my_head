import random
number1 = random.randint(1, 10)
number2 = random.randint(1, 10)
print('Сколько будет :' + str(number1) + ' + ' + str(number2) + '?')
answer = input()
if answer == number1 + number2:  # баг , надо так int(answer)( он складывает строки а надо int)
    print('верно!')
else:
    print('Нет, правильный ответ - ' + str(number1 + number2))
