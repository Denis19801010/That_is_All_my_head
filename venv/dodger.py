import pygame, random, sys
from pygame.locals import *

WINDOWWIDTH = 600
WINDOWHEIGHT = 600
TEXTCOLOR = (0, 0, 0)
BACKGROUNDCOLOR = (255, 255, 255)
FPS = 60
BADDEMINSIZE = 10
BADDEMINMAXSIZE = 40
BADDEMINSPEED = 1
BADDEMINMAXSPEED = 8
ADDNEWBADDIERATE = 6
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
pygame.mouse.set_visible(False)

# настройка шрифтов
font = pygame.font.SysFont(None, 35)

# настройка звуков
gameOverSound = pygame.mixer.Sound('gameover.wav')
pygame.mixer.music.load('1background.mid')

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
    score - 0
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



