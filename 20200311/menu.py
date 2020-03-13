import pygame
import main
import time
from pygame.locals import *

red = (200,0,0)
green = (0,200,0)
blue = (0,0,200)
white = (255,255,255)
wdw=pygame.display.set_mode((1600,880))
# pour savoir de quel niveau il sort
niveau = int
# Pour savoir si quand il sort du niveau, il est fini
toutfini = int
def menuprincipal():
    fond = pygame.image.load("sprite/menu.png").convert_alpha()
    wdw.blit(fond, (0,0))
    pygame.display.set_caption("Baba Is You")
    perso = pygame.image.load("sprite/persoDown.png").convert_alpha()
    wdw.blit(perso, (200,300))
    btclose = pygame.draw.rect(wdw, red,(1100,640,200,100))
    bt2 = pygame.draw.rect(wdw, green,(300,640,200,100))
    btlevel = pygame.draw.rect(wdw, blue,(700,220,200,100))
    pygame.display.update()
    continuer = True
    while continuer:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    if btclose.collidepoint(event.pos):
                        pygame.quit()
                        quit()
                if event.button == 1:
                    if btlevel.collidepoint(event.pos):
                        menulevel()
            if event.type == pygame.QUIT:
                print("\nArrêt")
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE :
                    print("\nArrêt")
                    pygame.quit()
                    quit()
def menulevel():
    # pour savoir de quel niveau il sort
    niveau = int
    # Pour savoir si quand il sort du niveau, il est fini
    toutfini = 0
    continuer = True
    fond = pygame.image.load("sprite/menu.png").convert_alpha()
    wdw.blit(fond, (0,0))
    btback = pygame.draw.rect(wdw, red,(1100,440,200,100))
    btlevel_1 = pygame.draw.rect(wdw, blue,(400,220,200,100))
    btlevel_2 = pygame.draw.rect(wdw, blue,(650,220,200,100))
    pygame.display.update()
    while continuer == True:
        for event in pygame.event.get():
                if event.type == MOUSEBUTTONUP:
                    if event.button == 1:
                        if btlevel_1.collidepoint(event.pos):
                            niveau, toutfini = main.jeu(1)
                            print("Dans menu level, niveau = {0}. Il a fini {1}".format(niveau, toutfini))
                        if btlevel_2.collidepoint(event.pos):
                            niveau, toutfini = main.jeu(2)
                            print("Dans menu level, niveau = {0}. Il a fini {1}".format(niveau, toutfini))
                        if btback.collidepoint(event.pos):
                            menuprincipal()
                        #toutfini : Si = 1 : il a fini le niveau, si = 0 il ne l'a pas fini, si = 2 : il est mort
                        if toutfini == 1:
                            time.sleep(1)
                            menuprincipal()
                        elif toutfini == 0:
                            time.sleep(0.5)
                            menuprincipal()
                        elif toutfini == 2:
                            time.sleep(0.5)
                            menuprincipal()
#pour que menuprincipal() ne ce lance pas quand on importe le fichier
if __name__ == '__main__':
    menuprincipal()
