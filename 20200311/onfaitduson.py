import pygame
from pygame.locals import *
def bandeson(debut):
    if debut == 0:
        musiquejeu = pygame.mixer.Sound("Sound/bandeson.mp3")
        pygame.mixer.music.load('Sound/bandeson.mp3')
        pygame.mixer.music.play(loops=-1)
        pygame.mixer.music.set_volume(0.5)
