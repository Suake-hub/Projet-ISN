from numpy import *
import time 
import pygame
from pygame.locals import *
from deplacements import *
from gammeplay import *
from actuallise import *
from level import *
debug = 1
wdw=pygame.display.set_mode((1600,880))
#Dans le tableau: 0 = sol; 1 = mur; 2 = caillou; 3 = drapeau; 4 = piques, 5 = caillou dans le trou, 6 = bouton, 7 = porte
#on importe toute les images
mur = pygame.image.load("sprite/Mur.png").convert_alpha()
sol = pygame.image.load("sprite/Sol.png").convert_alpha()
flag = pygame.image.load("sprite/flag.png").convert_alpha()
rock = pygame.image.load("sprite/rock.png").convert_alpha()
win = pygame.image.load("sprite/win2.png").convert_alpha()
defeat = pygame.image.load("sprite/death.png").convert_alpha()
spike = pygame.image.load("sprite/piques.png").convert_alpha()
setr = pygame.image.load("sprite/p+c.png").convert_alpha()
door = pygame.image.load("sprite/closedoor.png").convert_alpha()
buton = pygame.image.load("sprite/redbuton.png").convert_alpha()
perso2 = pygame.image.load("sprite/persoUp.png").convert_alpha()
perso1 = pygame.image.load("sprite/persoDown.png").convert_alpha()
perso4 = pygame.image.load("sprite/persoRight.png").convert_alpha()
perso3 = pygame.image.load("sprite/persoLeft.png").convert_alpha()
#
#on initialise les variables
def jeu(niveau):
    etat=int
    curX,curY = [9, 1]
    curXpast = int
    curYpast = int
    npdt = int
    npdtp = int
    porte = 1
    etat = 1
    tour = 0
    salle = niveaux(niveau)
    tour, curXpast, curYpast, npdt, npdtp, porte = refresh(wdw, debug, salle, curX, curY, mur, sol, flag, rock, win, defeat, spike, setr, door, buton, perso1, perso2, perso3, perso4, etat, tour, curXpast, curYpast, npdt, npdtp, porte)
    etat = 0
    salle = gameplay(curX, curY, wdw, salle, porte, etat, debug, tour, curXpast, curYpast, npdt, npdtp)
