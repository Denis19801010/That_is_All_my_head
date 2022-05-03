import pygame, sys, time, random
from pygame.locals import *

# установка pygame
pygame.init()
mainClock = pygame.time.Clock()

# настройка окна
WINDOWWIDTH = 700
WINDOWHEIGHT = 700
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Sounds and Sprites')

# настрйока цветов
WHITE = (255, 255, 255)

# создание структур данных блока
player = pygame.Rect(300, 100, 40, 40)
playerImage = pygame.image.load('player.png')
playerStretchedImage = pygame.transform.scale(playerImage, (40, 40))
foodImage = pygame.image.load('cherry.png')
foods = []
for i in range(20):
    foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH-20), random.randint(0, WINDOWHEIGHT-20), 20, 20))

foodCounter = 0
NEWFOOD = 60    # скорость добавления еды

    # создание переменных перемещения
moveLeft = False
moveRight = False
moveUp = False
moveDown = False

MOVESPEED = 6

# настройка музыки
pickUpSound = pygame.mixer.Sound('pickup.mp3')
pygame.mixer.music.load('background.mp3')
pygame.mixer.music.play(-1, 0.0)
musicPlaying = True

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
            if event.key == K_m: # включает/отключает музыку кнопкой М
                if musicPlaying:
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play(-1, 0.0)
                musicPlaying = not musicPlaying

        if event.type == MOUSEBUTTONUP:  # когда игрок перемещает мышь по окну.
            foods.append(pygame.Rect(event.pos[0] - 10, event.pos[1] - 10, 20, 20))

    foodCounter += 1
    if foodCounter >= NEWFOOD:
        # добавление новой "еды"
        foodCounter = 0
        foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - 20), random.randint(0, WINDOWHEIGHT - 20), 20, 20))

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


    # отображение блока на поверхности
    windowSurface.blit(playerStretchedImage, player)

    # проверка не пересёкся игрок с каким либо блоком "еды"
    for food in foods[:]:
        if player.colliderect(food):
            foods.remove(food)
            player = pygame.Rect(player.left, player.top, player.width + 2, player.height + 2)
            playerStretchedImage = pygame.transform.scale(playerImage, (player.width, player.height))
            if musicPlaying:
                pickUpSound.play()

    # отображение еды
    for food in foods:
        windowSurface.blit(foodImage, food)

    # вывод окна на экран
    pygame.display.update()
    mainClock.tick(80 )