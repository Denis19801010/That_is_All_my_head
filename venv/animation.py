import pygame, sys, time
from pygame.locals import *

# установка pygame
pygame.init()

# настройка окна
WINDOWWIDTH = 400
WINDOWWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWWHEIGHT), 0, 32)
pygame.display.set_caption('Animation')

# создание переменных направления
DOWNLEFT = 'downleft'
DOWNRIGHT = 'downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'

MOVESSPEED = 3

# настройка цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 255)
BLUE  = (0, 0, 255)

# создание структуры данных блоков
b1 = {'rect':pygame.Rect(300, 80, 50, 100), 'color':RED, 'dir':UPRIGHT}
b2 = {'rect':pygame.Rect(200, 200, 20, 20), 'color':GREEN, 'dir':UPLEFT}
b3 = {'rect':pygame.Rect(100, 150, 60, 60), 'color':BLUE, 'dir':DOWNLEFT}
boxes = [b1, b2, b3]

# запуск игрового цикла
while True:
    # проверка наличия события QUIT
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # создание поверхности белого фона
    windowSurface.fill(WHITE)

    for b in boxes:
        # перемещение структуры данных блока
        if b['dir'] == DOWNLEFT:
            b['rect'].left -= MOVESSPEED
            b['rect'].top += MOVESSPEED
        if b['dir'] == DOWNRIGHT:
            b['rect'].left -= MOVESSPEED
            b['rect'].top += MOVESSPEED
        if b['dir'] == UPLEFT:
            b['rect'].left -= MOVESSPEED
            b['rect'].top -= MOVESSPEED
        if b['dir'] == UPRIGHT:
            b['rect'].left += MOVESSPEED
            b['rect'].top -= MOVESSPEED

        # проверка преместился ли блок за пределы окна
        if b['rect'].top < 0:
            # прохождение блока через верхнюю границу
            if b['dir'] == UPLEFT:
                b['dir'] = DOWNLEFT
            if b['dir'] == UPRIGHT:
                b['dir'] = DOWNRIGHT
        if b['rect'].bottom > WINDOWWHEIGHT:
            # прохождение блока через нижнюю границу
            if b['dir'] == DOWNLEFT:
                b['dir'] = UPLEFT
            if b['dir'] == DOWNRIGHT:
                b['dir'] = UPRIGHT
        if b['rect'].left < 0:
            # прохождение блока через левую границу
            if b['dir'] == DOWNLEFT:
                b['dir'] = DOWNRIGHT
            if b['dir'] == UPLEFT:
                b['dir'] = UPRIGHT
        if b['rect'].right > WINDOWWIDTH:
            # прохождение блока через правую границу
            if b['dir'] == DOWNRIGHT:
                b['dir'] = DOWNLEFT
            if b['dir'] == UPRIGHT:
                b['dir'] = UPLEFT

        # создание блока на поверхности
        pygame.draw.rect(windowSurface, b['color'], b['rect'])

    # вывод окна на экран
    pygame.display.update()
    time.sleep(0.02)