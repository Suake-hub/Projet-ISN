from numpy import *
import time 
import pygame
from pygame.locals import *
from deplacements import *
from actuallise import *
def gameplay(curX, curY, wdw, salle, porte, etat, debug, tour, curXpast, curYpast, npdt, npdtp):
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
    cailX=int
    cailY=int
    status=int
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_DOWN:
                    etat = 1
                    curX, curY, status, porte = push(curX, curY, salle, debug, etat, wdw, porte)
                    if debug ==1:
                        print("\ncurX={0} \ncurY={1} \nstatus={2} \netat={3}".format(curX, curY, status, etat))
                    if salle[curX, curY] == 2:
                        salle[curX, curY] = 0
                        verifc=0
                        cailX, cailY = curX, curY
                        while verifc==0:
                            if debug == 1 :
                                print("\ncailX {0}\ncailY {1}".format(cailX,cailY))
                            if salle[cailX+1, cailY] == 0 or salle[cailX+1, cailY] == 3 or salle[cailX+1, cailY] == 6:
                                verifc=1
                                salle[cailX+1, cailY] = 2
                            elif salle[cailX+1, cailY] == 4:
                                verifc=1
                                salle[cailX+1, cailY] = 5
                            elif salle[cailX+1, cailY] == 2:
                                cailX = cailX+1
                            elif salle[cailX+1, cailY] == 7:
                                if porte == 0:
                                    verifc=1
                                    salle[cailX+1, cailY] = 2
                            elif  salle[cailX+1, cailY] == 5:
                                verifc=1
                                salle[cailX+1, cailY] = 8
                            elif  salle[cailX+1, cailY] == 8:
                                cailX = cailX+1
                            if event.key == pygame.K_ESCAPE:
                                if debug ==1:
                                    print("\nArrêt")
                                pygame.quit()
                                quit()
                    if salle[curX, curY] == 8:
                        salle[curX, curY] = 5
                        verifc=0
                        cailX, cailY = curX, curY
                        while verifc==0:
                            if debug == 1 :
                                print("\ncailX {0}\ncailY {1}".format(cailX,cailY))
                            if salle[cailX+1, cailY] == 0 or salle[cailX+1, cailY] == 3 or salle[cailX+1, cailY] == 6:
                                verifc=1
                                salle[cailX+1, cailY] = 2
                            elif salle[cailX+1, cailY] == 4:
                                verifc=1
                                salle[cailX+1, cailY] = 5
                            elif salle[cailX+1, cailY] == 2:
                                cailX = cailX+1
                            elif salle[cailX+1, cailY] == 7:
                                if porte == 0:
                                    verifc=1
                                    salle[cailX+1, cailY] = 2
                            elif  salle[cailX+1, cailY] == 5:
                                verifc=1
                                salle[cailX+1, cailY] = 8
                            elif  salle[cailX+1, cailY] == 8:
                                cailX = cailX+1
                            if event.key == pygame.K_ESCAPE:
                                if debug ==1:
                                    print("\nArrêt")
                                pygame.quit()
                                quit()
                    tour, curXpast, curYpast, npdt, npdtp, porte = refresh(wdw, debug, salle, curX, curY, mur, sol, flag, rock, win, defeat, spike, setr, door, buton, perso1, perso2, perso3, perso4, etat, tour, curXpast, curYpast, npdt, npdtp, porte)
                if event.key == pygame.K_UP:
                    etat = 2
                    curX, curY, status, porte = push(curX, curY, salle, debug, etat, wdw, porte)
                    if debug == 1:
                        print("\ncurX={0} \ncurY={1} \nstatus={2} \netat={3}".format(curX, curY, status, etat))
                    if salle[curX, curY] == 2:
                        salle[curX, curY] = 0
                        verifc=0
                        cailX, cailY = curX, curY
                        while verifc==0:
                            if debug == 1 :
                                print("\ncailX {0}\ncailY {1}".format(cailX,cailY))
                            if salle[cailX-1, cailY] == 0 or salle[cailX-1, cailY] == 3 or salle[cailX-1, cailY] == 6:
                                verifc=1
                                salle[cailX-1, cailY] = 2
                            elif salle[cailX-1, cailY] == 4:
                                verifc=1
                                salle[cailX-1, cailY] = 5
                            elif salle[cailX-1, cailY] == 2:
                                cailX = cailX-1
                            elif salle[cailX-1, cailY] == 7:
                                if porte == 0:
                                    verifc=1
                                    salle[cailX-1, cailY] = 2
                            elif  salle[cailX-1, cailY] == 5:
                                verifc=1
                                salle[cailX-1, cailY] = 8
                            elif  salle[cailX-1, cailY] == 8:
                                cailX = cailX-1
                            if event.key == pygame.K_ESCAPE:
                                if debug ==1:
                                    print("\nArrêt")
                                pygame.quit()
                                quit()
                    if salle[curX, curY] == 8:
                        salle[curX, curY] = 5
                        verifc=0
                        cailX, cailY = curX, curY
                        while verifc==0:
                            if debug == 1 :
                                print("\ncailX {0}\ncailY {1}".format(cailX,cailY))
                            if salle[cailX-1, cailY] == 0 or salle[cailX-1, cailY] == 3 or salle[cailX-1, cailY] == 6:
                                verifc=1
                                salle[cailX-1, cailY] = 2
                            elif salle[cailX-1, cailY] == 4:
                                verifc=1
                                salle[cailX-1, cailY] = 5
                            elif salle[cailX-1, cailY] == 2:
                                cailX = cailX-1
                            elif salle[cailX-1, cailY] == 7:
                                if porte == 0:
                                    verifc=1
                                    salle[cailX-1, cailY] = 2
                            elif  salle[cailX-1, cailY] == 5:
                                verifc=1
                                salle[cailX-1, cailY] = 8
                            elif  salle[cailX-1, cailY] == 8:
                                cailX = cailX-1
                            if event.key == pygame.K_ESCAPE:
                                if debug ==1:
                                    print("\nArrêt")
                                pygame.quit()
                                quit()
                    tour, curXpast, curYpast, npdt, npdtp, porte = refresh(wdw, debug, salle, curX, curY, mur, sol, flag, rock, win, defeat, spike, setr, door, buton, perso1, perso2, perso3, perso4, etat, tour, curXpast, curYpast, npdt, npdtp, porte)
                if event.key == pygame.K_LEFT:
                    etat = 3
                    curX, curY, status, porte = push(curX, curY, salle, debug, etat, wdw, porte)
                    if debug == 1:
                        print("\ncurX={0} \ncurY={1} \nstatus={2} \netat={3}".format(curX, curY, status, etat))
                    if salle[curX, curY] == 2:
                        salle[curX, curY] = 0
                        verifc=0
                        cailX, cailY = curX, curY
                        while verifc==0:
                            if debug == 1 :
                                print("\ncailX {0}\ncailY {1}".format(cailX,cailY))
                            if salle[cailX, cailY-1] == 0 or salle[cailX, cailY-1] == 3 or salle[cailX, cailY-1] == 6:
                                verifc=1
                                salle[cailX, cailY-1] = 2
                            elif salle[cailX, cailY-1] == 4:
                                verifc=1
                                salle[cailX, cailY-1] = 5
                            elif salle[cailX, cailY-1] == 2:
                                cailY = cailY-1
                            elif salle[cailX, cailY-1] == 7:
                                if porte == 0:
                                    verifc=1
                                    salle[cailX, cailY-1] = 2
                            elif  salle[cailX, cailY-1] == 5:
                                verifc=1
                                salle[cailX, cailY-1] = 8
                            elif  salle[cailX, cailY-1] == 8:
                                cailY = cailY-1
                            if event.key == pygame.K_ESCAPE:
                                if debug ==1:
                                    print("\nArrêt")
                                pygame.quit()
                                quit()
                    if salle[curX, curY] == 8:
                        salle[curX, curY] = 5
                        verifc=0
                        cailX, cailY = curX, curY
                        while verifc==0:
                            if debug == 1 :
                                print("\ncailX {0}\ncailY {1}".format(cailX,cailY))
                            if salle[cailX, cailY-1] == 0 or salle[cailX, cailY-1] == 3 or salle[cailX, cailY-1] == 6:
                                verifc=1
                                salle[cailX, cailY-1] = 2
                            elif salle[cailX, cailY-1] == 4:
                                verifc=1
                                salle[cailX, cailY-1] = 5
                            elif salle[cailX, cailY-1] == 2:
                                cailY = cailY-1
                            elif salle[cailX, cailY-1] == 7:
                                if porte == 0:
                                    verifc=1
                                    salle[cailX, cailY-1] = 2
                            elif  salle[cailX, cailY-1] == 5:
                                verifc=1
                                salle[cailX, cailY-1] = 8
                            elif  salle[cailX, cailY-1] == 8:
                                cailY = cailY-1
                            if event.key == pygame.K_ESCAPE:
                                if debug ==1:
                                    print("\nArrêt")
                                pygame.quit()
                                quit()
                    tour, curXpast, curYpast, npdt, npdtp, porte = refresh(wdw, debug, salle, curX, curY, mur, sol, flag, rock, win, defeat, spike, setr, door, buton, perso1, perso2, perso3, perso4, etat, tour, curXpast, curYpast, npdt, npdtp, porte)
                if event.key == pygame.K_RIGHT:
                    etat = 4 
                    curX, curY, status, porte = push(curX, curY, salle, debug, etat, wdw, porte)
                    if debug == 1:
                        print("\ncurX={0} \ncurY={1} \nstatus={2} \netat={3}".format(curX, curY, status, etat))
                    if salle[curX, curY] == 2:
                        salle[curX, curY] = 0
                        verifc=0
                        cailX, cailY = curX, curY
                        while verifc==0:
                            if debug == 1 :
                                print("\ncailX {0}\ncailY {1}".format(cailX,cailY))
                            if salle[cailX, cailY+1] == 0 or salle[cailX, cailY+1] == 3 or salle[cailX, cailY+1] == 6:
                                verifc=1
                                salle[cailX, cailY+1] = 2
                            elif salle[cailX, cailY+1] == 4:
                                verifc=1
                                salle[cailX, cailY+1] = 5
                            elif salle[cailX, cailY+1] == 2:
                                cailY = cailY+1
                            elif salle[cailX, cailY+1] == 7:
                                if porte == 0:
                                    verifc=1
                                    salle[cailX, cailY+1] = 2
                            elif  salle[cailX, cailY+1] == 5:
                                verifc=1
                                salle[cailX, cailY+1] = 8
                            elif  salle[cailX, cailY+1] == 8:
                                cailY = cailY+1
                            if event.key == pygame.K_ESCAPE:
                                if debug ==1:
                                    print("\nArrêt")
                                pygame.quit()
                                quit()
                    if salle[curX, curY] == 8:
                        salle[curX, curY] = 5
                        verifc=0
                        cailX, cailY = curX, curY
                        while verifc==0:
                            if debug == 1 :
                                print("\ncailX {0}\ncailY {1}".format(cailX,cailY))
                            if salle[cailX, cailY+1] == 0 or salle[cailX, cailY+1] == 3 or salle[cailX, cailY+1] == 6:
                                verifc=1
                                salle[cailX, cailY+1] = 2
                            elif salle[cailX, cailY+1] == 4:
                                verifc=1
                                salle[cailX, cailY+1] = 5
                            elif salle[cailX, cailY+1] == 2:
                                cailY = cailY+1
                            elif salle[cailX, cailY+1] == 7:
                                if porte == 0:
                                    verifc=1
                                    salle[cailX, cailY+1] = 2
                            elif  salle[cailX, cailY+1] == 5:
                                verifc=1
                                salle[cailX, cailY+1] = 8
                            elif  salle[cailX, cailY+1] == 8:
                                cailY = cailY+1
                            if event.key == pygame.K_ESCAPE:
                                if debug ==1:
                                    print("\nArrêt")
                                pygame.quit()
                                quit()
                    tour, curXpast, curYpast, npdt, npdtp, porte = refresh(wdw, debug, salle, curX, curY, mur, sol, flag, rock, win, defeat, spike, setr, door, buton, perso1, perso2, perso3, perso4, etat, tour, curXpast, curYpast, npdt, npdtp, porte)
                if event.key == pygame.K_ESCAPE:
                    if debug ==1:
                        print("\nArrêt")
                    pygame.quit()
                    quit()
                if salle[curX, curY] == 3:
                    finilevel(niveau, wdw, win)
