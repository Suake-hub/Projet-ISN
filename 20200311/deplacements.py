import pygame
import time
def push(curX, curY, salle, debug, etat, wdw, porte):
    status=int
    #si dans la direction 0 alors bouger/return
    if etat == 1:
        if salle[curX+1, curY] == 0:
            curY, curX = curY, curX+1
            return curX, curY, status, porte
    if etat == 2:
        if salle[curX-1, curY] == 0:
            curY, curX = curY, curX-1
            return curX, curY, status, porte
    if etat == 3:
        if salle[curX, curY-1] == 0:
            curY, curX = curY-1, curX
            return curX, curY, status, porte
    if etat == 4:
        if salle[curX, curY+1] == 0:
            curY, curX = curY+1, curX
            return curX, curY, status, porte
    # si dans la direction mur alors change image et return
    if etat == 1:
        if salle[curX+1, curY] == 1:
            return curX, curY, status, porte
    if etat == 2:
        if salle[curX-1, curY] == 1:
            return curX, curY, status, porte
    if etat == 3:
        if salle[curX, curY-1] == 1:
            return curX, curY, status, porte
    if etat == 4:
        if salle[curX, curY+1] == 1:
            return curX, curY, status, porte
    # si il y a un caillou, check si 0 il vas dessus, si 1 change etat et return
    if etat == 1:
        if salle[curX+1, curY] == 2:
            status=check(curX, curY, salle, debug, etat, wdw, status, porte)
            print("status{0}".format(status))
    if etat == 2:
        if salle[curX-1, curY] == 2:
            status=check(curX, curY, salle, debug, etat, wdw, status, porte)
            print("status{0}".format(status))
    if etat == 3:
        if salle[curX, curY-1] == 2:
            status=check(curX, curY, salle, debug, etat, wdw, status, porte)
            print("status{0}".format(status))
    if etat == 4:
        if salle[curX, curY+1] == 2:
            status=check(curX, curY, salle, debug, etat, wdw, status, porte)
            print("status{0}".format(status))
    #si il y a un drapeau, il vas dessus
    if etat == 1:
        if salle[curX+1, curY] == 3:
            curY, curX = curY, curX+1
            return curX, curY, status, porte
    if etat == 2:
        if salle[curX-1, curY] == 3:
            curY, curX = curY, curX-1
            return curX, curY, status, porte
    if etat == 3:
        if salle[curX, curY-1] == 3:
            curY, curX = curY-1, curX
            return curX, curY, status, porte
    if etat == 4:
        if salle[curX, curY+1] == 3:
            curY, curX = curY+1, curX
            return curX, curY, status, porte
    #si il y a un pique, il vas dessus
    if etat == 1:
        if salle[curX+1, curY] == 4:
            curY, curX = curY, curX+1
            return curX, curY, status, porte
    if etat == 2:
        if salle[curX-1, curY] == 4:
            curY, curX = curY, curX-1
            return curX, curY, status, porte
    if etat == 3:
        if salle[curX, curY-1] == 4:
            curY, curX = curY-1, curX
            return curX, curY, status, porte
    if etat == 4:
        if salle[curX, curY+1] == 4:
            curY, curX = curY+1, curX
            return curX, curY, status, porte
    #si il y a un "move", il le vas dessus
    if etat == 1:
        if salle[curX+1, curY] == 5:
            curY, curX = curY, curX+1
            return curX, curY, status, porte
    if etat == 2:
        if salle[curX-1, curY] == 5:
            curY, curX = curY, curX-1
            return curX, curY, status, porte
    if etat == 3:
        if salle[curX, curY-1] == 5:
            curY, curX = curY-1, curX
            return curX, curY, status, porte
    if etat == 4:
        if salle[curX, curY+1] == 5:
            curY, curX = curY+1, curX
            return curX, curY, status, porte
    #si il y a un bouton, vas dessus
    if etat == 1:
        if salle[curX+1, curY] == 6:
            curY, curX = curY, curX+1
            return curX, curY, status, porte
    if etat == 2:
        if salle[curX-1, curY] == 6:
            curY, curX = curY, curX-1
            return curX, curY, status, porte
    if etat == 3:
        if salle[curX, curY-1] == 6:
            curY, curX = curY-1, curX
            return curX, curY, status, porte
    if etat == 4:
        if salle[curX, curY+1] == 6:
            curY, curX = curY+1, curX
            return curX, curY, status, porte
    #si il y a une porte, regarde si il peut passer
    if etat == 1:
        if salle[curX+1, curY] == 7:
            if porte == 0:
                curY, curX = curY, curX+1
                return curX, curY, status, porte
            elif porte == 1:
                return curX, curY, status, porte
    if etat == 2:
        if salle[curX-1, curY] == 7:
            if porte == 0:
                curY, curX = curY, curX-1
                return curX, curY, status, porte
            elif porte == 1:
                return curX, curY, status, porte
    if etat == 3:
        if salle[curX, curY-1] == 7:
            if porte == 0:
                curY, curX = curY-1, curX
                return curX, curY, status, porte
            if porte == 1:
                return curX, curY, status, porte
    if etat == 4:
        if salle[curX, curY+1] == 7:
            if porte == 0:
                curY, curX = curY+1, curX
                return curX, curY, status, porte
            if porte == 1:
                return curX, curY, status, porte
        # si il y a un caillou sur un caillou dans un trou, check si 0 il vas dessus, si 1 change etat et return
    if etat == 1:
        if salle[curX+1, curY] == 8:
            status=check(curX, curY, salle, debug, etat, wdw, status, porte)
            print("status{0}".format(status))
    if etat == 2:
        if salle[curX-1, curY] == 8:
            status=check(curX, curY, salle, debug, etat, wdw, status, porte)
            print("status{0}".format(status))
    if etat == 3:
        if salle[curX, curY-1] == 8:
            status=check(curX, curY, salle, debug, etat, wdw, status, porte)
            print("status{0}".format(status))
    if etat == 4:
        if salle[curX, curY+1] == 8:
            status=check(curX, curY, salle, debug, etat, wdw, status, porte)
            print("status{0}".format(status))
            
    #deplacements
    if status == 0:
        if etat == 1:
            curX, curY = curX+1, curY
        if etat == 2:
            curX, curY = curX-1, curY
        if etat == 3:
            curX, curY = curX, curY-1
        if etat == 4:
            curX, curY = curX, curY+1
    return curX, curY, status, porte

        
def check(curX, curY, salle, debug, etat, wdw, status, porte):
    if etat == 1:
        if salle[curX+1, curY] == 1 or salle[curX+1, curY] == 3 or salle[curX+1, curY] == 6:
            status = 1
            return status
        elif salle[curX+1, curY] == 0 or salle[curX+1, curY] == 4 or salle[curX+1, curY] == 5:
            status = 0
            return status
        elif salle[curX+1, curY] == 2 or salle[curX+1, curY] == 8:
            status=check(curX+1, curY, salle, debug, etat, wdw, status, porte)
            if debug == 1:
                print("La case devant est : {0}".format(salle[curX+1, curY]))
        elif salle[curX+1, curY] == 7:
            if porte == 0:
                status = 0
                return status
            elif porte == 1:
                status = 1
                return status
    if etat == 2:
        if salle[curX-1, curY] == 1  or salle[curX-1, curY] == 3 or salle[curX-1, curY] == 6:
            status = 1
            return status
        elif salle[curX-1, curY] == 0 or salle[curX-1, curY] == 4 or salle[curX-1, curY] == 5:
            status = 0
            return status
        elif salle[curX-1, curY] == 2 or salle[curX-1, curY] == 8:
            status=check(curX-1, curY, salle, debug, etat, wdw, status, porte)
            if debug == 1:
                print("La case devant est : {0}".format(salle[curX+1, curY]))
        elif salle[curX-1, curY] == 7:
            if porte == 0:
                status = 0
                return status
            elif porte == 1:
                status = 1
                return status
    if etat == 3:
        if salle[curX, curY-1] == 1 or salle[curX, curY-1] == 3 or salle[curX, curY-1] == 6:
            status = 1
            return status
        elif salle[curX, curY-1] == 0 or salle[curX, curY-1] == 4 or salle[curX, curY-1] == 5:
            status = 0
            return status
        elif salle[curX, curY-1] == 2 or salle[curX, curY-1] == 8:
            status=check(curX, curY-1, salle, debug, etat, wdw, status, porte)
            if debug == 1:
                print("La case devant est : {0}".format(salle[curX+1, curY]))
        elif salle[curX, curY-1] == 7:
            if porte == 0:
                status = 0
                return status
            elif porte == 1:
                status = 1
                return status
    if etat == 4:
        if salle[curX, curY+1] == 1 or salle[curX, curY+1] == 3 or salle[curX, curY+1] == 6:
            status = 1
            return status
        elif salle[curX, curY+1] == 0 or salle[curX, curY+1] == 4 or salle[curX, curY+1] == 5:
            status = 0
            return status
        elif salle[curX, curY+1] == 2 or salle[curX, curY+1] == 8:
            status=check(curX, curY+1, salle, debug, etat, wdw, status, porte)
            if debug == 1:
                print("La case devant est : {0}".format(salle[curX+1, curY]))
        elif salle[curX, curY+1] == 7:
            if porte == 0:
                status = 0
                return status
            elif porte == 1:
                status = 1
                return status
    return status
