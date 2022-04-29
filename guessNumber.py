#  Это игра по угадыванию чисел
import random

guessesTaken = 0  # Эта переменная будет хранить количество попыток игрока угадать число.
                 #   Так как на этом этапе программы игрок не сделал ни одной попытки, мы при-
                 # сваиваем ей целое значение

print("Привет! Как тебя зовут? ")

myName = input()

number = random.randint(1, 20)  # загадывает число от 1 до 20

print("Ну привет " + myName + " Я сейчас загадаю число от 1 до 20, а ты угадай с 4 попыток ")

for guessesTaken in range(4):
    print(" а ну ка блесни знаниями, попробуй давай")
    guess = input()  # input  всегда строковое, поэтому переводим его в число
    guess = int(guess)

    if guess < number:
        print("хрен та там, оно больше. давай дальше ")

    if guess > number:
        print("перебор, давай поменьше")

    if guess == number:
        print("угадал")
        break
if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print("На этот раз тебе повезло, ты угадал с " + guessesTaken + " попытки")

if guess != number:
    number = str(number)
    print("нифига не угадал, число было " + number)



