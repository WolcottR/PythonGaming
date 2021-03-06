#!/usr/bin/python
import pygame
from pygame.locals import *

# import system modules
from glob import glob

def main():
    # initialize screen
    pygame.init()
    screen = pygame.display.set_mode((150,50))
    pygame.display.set_caption('Basic Pygame program')

    # fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    # display some text
    font = pygame.font.Font(None, 36)
    text = font.render("Hello There", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    count = False
    list = [ i for i in glob("/usr/share/sounds/gnome/default/alerts/*.ogg")]

    pygame.mixer.init()
    pygame.mixer.music.load(list[0])
    pygame.mixer.music.play()

    for i in list[1:]:
        pygame.mixer.music.queue(i)

    # queue doesn't seem to be working
    # pygame.mixer.music.queue("/usr/share/sounds/gnome/default/alerts/bark.ogg")

    # Event loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.mixer.music.stop()
                return

        screen.blit(background, (0, 0))
        pygame.display.flip()

if __name__=='__main__': main()
    
