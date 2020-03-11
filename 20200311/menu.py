import pygame
import main
from pygame.locals import *

red = (200,0,0)
green = (0,200,0)
blue = (0,0,200)
white = (255,255,255)
wdw=pygame.display.set_mode((1600,880))

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
                            main.jeu(1)
                        if btlevel_2.collidepoint(event.pos):
                            main.jeu(2)
                        if btback.collidepoint(event.pos):
                            menuprincipal()
menuprincipal()
