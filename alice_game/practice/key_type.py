import sys

import pygame

def key_type():

    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("Key Type")

    while True:
        for event in pygame.event.get():
            #print(event.key)
            print(event.type)
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(event.key)

key_type()