import pygame, sys, random
from pygame.locals import *

# установка pygame
pygame.init()
mainClock = pygame.time.Clock()

# настройка окна
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Collision Detection')

# настрйока цветов
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# создание структур данных игрока и "еды"
foodCounter = 0
NEWFOOD = 40    # скорость добавления еды
FOODSIZE = 20
player = pygame.Rect(300, 100, 50, 50)
foods = []
for i in range(20):
    foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH-FOODSIZE), random.randint(0, WINDOWHEIGHT-FOODSIZE), FOODSIZE, FOODSIZE))

    # создание переменных перемещения
moveLeft = False
moveRight = False
moveUp = False
moveDown = False

MOVESPEED = 6


# запуск игрового цикла
while True:
    # проверка союытий
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:  # когда игрок нажимает клавишу.
            # изменение параметров клавиатуры
            if event.key == K_LEFT or event.key == K_a:  # K_a, K_d, K_w, K_s  это кнопки перемещения  w a s d
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT or event.key == K_d:
                moveLeft = False
                moveRight = True
            if event.key == K_UP or event.key == K_w:
                moveDown = False
                moveUp = True
            if event.key == K_DOWN or event.key == K_s:
                moveUp = False
                moveDown = True
        if event.type == KEYUP:  # когда игрок отпускает клавишу.
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == K_a:
                moveLeft = False
            if event.key == K_RIGHT or event.key == K_d:
                moveRight = False
            if event.key == K_UP or event.key == K_w:
                moveUp = False
            if event.key == K_DOWN or event.key == K_s:
                moveDown = False
            if event.key == K_x:
                player.top = random.randint(0, WINDOWHEIGHT - player.height)
                player.left = random.randint(0, WINDOWWIDTH - player.width)

        if event.type == MOUSEBUTTONUP:  # когда игрок перемещает мышь по окну.
            foods.append(pygame.Rect(event.pos[0], event.pos[1], FOODSIZE, FOODSIZE))

    foodCounter += 1
    if foodCounter >= NEWFOOD:
        # добавление новой "еды"
        foodCounter = 0
        foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))

   # создание поверхности белого фона
    windowSurface.fill(WHITE)

   # перемещение игрока
    if moveDown and player.bottom < WINDOWHEIGHT:
        player.top += MOVESPEED
    if moveUp and player.top > 0:
        player.top -= MOVESPEED
    if moveLeft and player.left > 0:
        player.left -= MOVESPEED
    if moveRight and player.right < WINDOWWIDTH:
        player.right += MOVESPEED

    # отображение игрока на поверхности
    pygame.draw.rect(windowSurface, BLACK, player)

    # проверка не пересёкся игрок с каким либо блоком "еды"
    for food in foods[:]:
        if player.colliderect(food):
            foods.remove(food)

    # отображение еды
    for i in range(len(foods)):
        pygame.draw.rect(windowSurface, GREEN, foods[i])

    # вывод окна на экран
    pygame.display.update()
    mainClock.tick(40 )