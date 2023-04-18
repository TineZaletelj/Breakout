import pygame
import time
import random

pygame.init()
pygame.font.init()
zaslon = pygame.display.set_mode((1000, 480))
myfont = pygame.font.SysFont('Comic Sans MS', 60, True)
laufej = 1

prva = pygame.image.load('1.jpg')
prva.convert()
druga = pygame.image.load('2.jpg')
druga.convert()
tretja = pygame.image.load('3.jpg')
tretja.convert()
cetrta = pygame.image.load('4.jpg')
cetrta.convert()

lvl = [0,0,0,0]

def premik(xpremik):    # premik spodnjega pravokotnika
    tipka = pygame.key.get_pressed()
    if tipka[pygame.K_LEFT]:
        if xpremik > 0:
            xpremik -= 2
    elif tipka[pygame.K_RIGHT]:
        if xpremik < 920:
            xpremik += 2
    return xpremik

#smeri
# 2\  /1
#   \/
#   /\
# 3/  \4

# odboji glede na to, ob kateri stranici se zgodijo
def zgoraj(smer):
    if smer == 2:
        smer = 3
    elif smer == 1:
        smer = 4
    return smer

def levo(smer):
    if smer == 2:
        smer = 1
    elif smer == 3:
        smer = 4
    return smer

def desno(smer):
    if smer == 1:
        smer = 2
    elif smer == 4:
        smer = 3
    return smer

def spodaj(smer):
    if smer == 3:
        smer = 2
    elif smer == 4:
        smer = 1
    return smer

smer = 1
def premikzoge(smer,xz,yz, xpremik):
    # sprememba smeri glede na rob zaslona
    if xz == 0:
        smer = levo(smer)
    if yz == 0:
        smer = zgoraj(smer)
    if xz == 985:
        smer = desno(smer)

    # odboj od spodnjega pravokotnika
    if yz == 425 and (xpremik - 8) <= xz <= (xpremik + 72):
        smer = spodaj(smer)

    # odboj od zgornjih pravokotnikov
    y=-20
    for b in kocke:
        x=10
        y+=30
        for i in range(10):
            if ((x - 10) <= xz <= (x+75)) and (yz == (y + 20)) and (b[i] > 0):
                b[i] -= 1
                if smer == 1 or smer == 2:
                    smer = zgoraj(smer)
                elif smer == 3:
                    smer = 4
                elif smer == 4:
                    smer = 3

            elif ((x - 10) <= xz <= (x + 75)) and (yz <= (y + 20)) and (b[i] > 0):
                b[i] -= 1
                if smer == 1 or smer == 4:
                    smer = desno(smer)
                elif smer == 2 or smer == 3:
                    smer = levo(smer)
            x += 100

    # premiki zoge glede na smer
    if smer == 1:   # desno gor
        xz += 1
        yz -= 1
    elif smer == 2:   # levo gor
        xz -= 1
        yz -= 1
    elif smer == 3:   # desno dol
        xz -= 1
        yz += 1
    elif smer == 4:   # levo gor
        xz += 1
        yz += 1
    return smer, xz, yz

def nivo():
    zaslon.fill(color=(255,230,255))
    text = myfont.render('Izberi težavnost-na tipkovnici', False, (0, 0, 0))
    zaslon.blit(text, (40, 20))
    text = myfont.render('klikni številko 1-4', False, (0, 0, 0))
    zaslon.blit(text, (40, 100))
    x=40
    y=200
    for i in lvl:
        if i == 1: # lvl je opravljen
            pygame.draw.rect(zaslon, color=(0,255,0), rect=(x,y,80,80))
        elif i == 0: # nivoja igralec še ni poskusil
            pygame.draw.rect(zaslon, color=(200, 200, 200), rect=(x, y, 80, 80))
        elif i == -1: # igralcu ni uspelo opraviti nivoja
            pygame.draw.rect(zaslon, color=(255, 0, 0), rect=(x, y, 80, 80))
        x+=100
    text = myfont.render('1', False, (0, 0, 0))
    zaslon.blit(text, (60, 200))
    text = myfont.render('2', False, (0, 0, 0))
    zaslon.blit(text, (160, 200))
    text = myfont.render('3', False, (0, 0, 0))
    zaslon.blit(text, (260, 200))
    text = myfont.render('4', False, (0, 0, 0))
    zaslon.blit(text, (360, 200))
    pygame.display.update()

    level =0
    while level==0: #program čaka na vnos igralca-izbira nivoja
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.unicode == '1':
                    level = 1
                elif event.unicode == '2':
                    level = 2
                elif event.unicode == '3':
                    level = 3
                elif event.unicode == '4':
                    level = 4
    return level

kocka=[
    [[0,0,0]],
    [[2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
    [[3, 3, 3, 3, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
    [[4, 4, 4, 4, 4, 4, 4, 4, 4, 4], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
    [[4, 4, 4, 4, 4, 4, 4, 4, 4, 4], [4, 4, 4, 3, 3, 3, 3, 4, 4, 4], [4, 3, 3, 2, 2, 2, 2, 3, 3, 4], [3, 3, 2, 2, 2, 2, 2, 2, 3, 3], [2, 2, 2, 1, 1, 1, 1, 2, 2, 2], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
       ]

level=0

while laufej:
    # če klikneš x se program zapre
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            laufej = 0
            pygame.quit()

    if level == 0: # ko level ni izbran, poženi funkcijo nivo in določi hitrost premikanja žoge glede na nivo
        level=nivo()
        kocke=kocka[level-1]
        if level == 1:
            cajt=0.006
        elif level == 2:
            cajt=0.005
        elif level == 3:
            cajt=0.004
        elif level == 4:
            cajt=0.003
        xpremik = random.randint(100, 800)  # zacetna pozicija sp pravokotnika
        xz = xpremik + 20  # pozicija zoge
        yz = 425

    # premik sp. pravokotnika
    xpremik = premik(xpremik)


    # barva ozadja
    zaslon.fill(color=(0, 210, 200))

    # risanje pravokotnikov
    y = -20
    for b in kocke:
        x = 10
        y += 30
        for i in b:
            if i==1:
                prav = prva.get_rect()
                prav.width=80
                prav.height=20
                zaslon.blit(prva, (x, y))
            elif i==2:
                prav = druga.get_rect()
                prav.width=80
                prav.height=20
                zaslon.blit(druga, (x, y))
            elif i==3:
                prav = tretja.get_rect()
                prav.width=80
                prav.height=20
                zaslon.blit(tretja, (x, y))
            elif i==4:
                prav = cetrta.get_rect()
                prav.width=80
                prav.height=20
                zaslon.blit(cetrta, (x, y))
            x += 100

    # premik pravokotnika + odboj in premik zoge
    smer, xz, yz = premikzoge(smer, xz, yz, xpremik)
    pygame.draw.rect(surface=zaslon, color=(255, 255, 255), rect=(xpremik, 440, 80, 20))
    pygame.draw.rect(surface=zaslon, color=(0, 0, 0), rect=(xz, yz, 15, 15))

    # poraz
    if yz == 465:
        zaslon.fill(color=(255, 0, 0))
        text = myfont.render('GAME OVER', False,  (0, 0, 0))
        zaslon.blit(text, (300, 180))
        pygame.display.update()
        time.sleep(3)
        lvl[level-1]=-1
        level=0
        smer=1

    # zmaga
    tocke = 0
    for b in kocke:
        tocke += sum(b)
    if tocke == 0:
        zaslon.fill(color=(0, 255, 0))
        text = myfont.render('BRAVO', False, (0, 0, 0))
        zaslon.blit(text, (300, 180))
        pygame.display.update()
        time.sleep(3)
        lvl[level-1]=1
        level=0
        smer=1

    time.sleep(cajt)



    pygame.display.update()



