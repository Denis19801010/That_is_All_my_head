import pygame, random, sys
from pygame.locals import *

WINDOWWIDTH = 800
WINDOWHEIGHT = 800
TEXTCOLOR = (0, 0, 0)
BACKGROUNDCOLOR = (255, 255, 100)
FPS = 60
BADDEMINSIZE = 20
BADDEMINMAXSIZE = 80
BADDEMINSPEED = 1
BADDEMINMAXSPEED = 2
ADDNEWBADDIERATE = 100
PLAYERMOVERATE = 5

def terminate():
    pygame.quit()
    sys.exit()

def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # ESC осуществляет выход
                    terminate()
                return

def playerHasHitBaddie(playerRect, baddies):
    for b in baddies:
        if playerRect.colliderect(b['rect']):
            return True
    return False

def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# настройка pygame, окна и указателя мыши
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Ловкач')
pygame.mouse.set_visible(False)  # делаем указатель мыши невидимый

# настройка шрифтов
font = pygame.font.SysFont(None, 35)

# настройка звуков
gameOverSound = pygame.mixer.Sound('gameover.mp3')
pygame.mixer.music.load('1background.mp3')

# настройка изображений
playerImage = pygame.image.load('1player.png')
playerRect = playerImage.get_rect()
baddieImage = pygame.image.load('baddie.png')

# вывод начального экрана
windowSurface.fill(BACKGROUNDCOLOR)
drawText('Ловкач', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
drawText('Нажмите клавишу начала игры', font, windowSurface, (WINDOWWIDTH/5)-30, (WINDOWHEIGHT/3)+50)
pygame.display.update()
waitForPlayerToPressKey()

topScore = 0
while True:
    # настройка начала игры
    baddies = []
    score = 0
    playerRect.topleft = (WINDOWWIDTH / 2, WINDOWHEIGHT -50)
    moveLeft = moveRight = moveUp = moveDown = False
    reverseCheat = slowCheat = False
    baddieAddCounter = 0
    pygame.mixer.music.play(-1, 0.0)

    while True:  # игровой цикл выполняется, пока игра работает
        score += 1  # увеличение количества очков

        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

            if event.type == KEYDOWN:
                if event.key == K_z:
                    reverseCheat = True
                if event.key == K_x:
                    slowCheat = True
                if event.key == K_LEFT or event.key == K_a:
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

            if event.type == KEYUP:
                if event.key == K_z:
                    reverseCheat = False
                    score = 0   # сбрасывает очки до 0, что бы не привыкать пользоваться читами
                if event.key == K_x:
                    slowCheat = False
                    score = 0  # сбрасывает очки до 0, что бы не привыкать пользоваться читами
                if event.key == K_ESCAPE:
                        terminate()

                if event.key == K_LEFT or event.key == K_a:
                    moveLeft = False
                if event.key == K_RIGHT or event.key == K_d:
                    moveRight = False
                if event.key == K_UP or event.key == K_w:
                    moveUp = False
                if event.key == K_DOWN or event.key == K_s:
                    moveDown = False

            if event.type == MOUSEMOTION:
                # если мышь движется, перенести игрока к указателю мыши(управление игрой с помощью мышки)
                playerRect.centerx = event.pos[0]
                playerRect.centery = event.pos[1]
        # если необходимо добавить новых злодеев в верхнюю часть экрана
        if not reverseCheat and not slowCheat:
            baddieAddCounter += 1
        if baddieAddCounter == ADDNEWBADDIERATE:
            baddieAddCounter = 0
            baddieSize = random.randint(BADDEMINSIZE, BADDEMINMAXSIZE)
            newBaddie = {'rect':pygame.Rect(random.randint(0, WINDOWWIDTH - baddieSize), 0 - baddieSize, baddieSize,
                                            baddieSize), 'speed':random.randint(BADDEMINSPEED,
                                            BADDEMINMAXSPEED), 'surface':pygame.transform.scale(baddieImage,
                                            (baddieSize, baddieSize))}

            baddies.append(newBaddie)

        # перемещение игрока по экрану
        if moveLeft and playerRect.left > 0:
            playerRect.move_ip(-1 * PLAYERMOVERATE, 0)
        if moveRight and playerRect.right < WINDOWWIDTH:
            playerRect.move_ip(PLAYERMOVERATE, 0)
        if moveUp and playerRect.top > 0:
            playerRect.move_ip(0, -1 * PLAYERMOVERATE)
        if moveDown and playerRect.bottom < WINDOWHEIGHT:
            playerRect.move_ip(0, PLAYERMOVERATE)

        # перемещение злодеев вниз
        for b in baddies:
            if not reverseCheat and not slowCheat:
                b['rect'].move_ip(0, b['speed'])
            elif reverseCheat:
                b['rect'].move_ip(0, -5)
            elif slowCheat:
                b['rect'].move_ip(0, 1)

        # удаление злодеев попавших за нижнюю границу экрана
        for b in baddies[:]:
            if b['rect'].top > WINDOWHEIGHT:
                baddies.remove(b)

        # отображение в окне игрового мира
        windowSurface.fill(BACKGROUNDCOLOR)

        # отображение количества очков и лучшего результата
        drawText('Счёт: %s ' % (score), font, windowSurface, 10, 0)
        drawText('Рекорд: %s ' % (topScore), font, windowSurface, 10, 40)

        # отображени етреугольника игрока
        windowSurface.blit(playerImage, playerRect)

        # отображение каждого злодея
        for b in baddies:
            windowSurface.blit(b['surface'], b['rect'])

        pygame.display.update()

        # проверка попал ли в игрока какой-нибудь злодей
        if playerHasHitBaddie(playerRect, baddies):
            if score > topScore:
                topScore = score  # установка нового рекорда
            break

            mainClock.tick(FPS)

        # отобраени еигры и вывод надписи игра окончена
    pygame.mixer.music.stop()
    gameOverSound.play()

    drawText(' Игра окончена!', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
    drawText('Нажми клавишу для начала новой игры ', font, windowSurface, (WINDOWWIDTH / 3) - 120, (WINDOWHEIGHT /
                                                                                                        3) + 50)
    pygame.display.update()
    waitForPlayerToPressKey()

    gameOverSound.stop()