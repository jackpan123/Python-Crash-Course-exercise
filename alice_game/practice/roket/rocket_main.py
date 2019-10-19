import sys

import pygame
import rocket_functions as rf

from setting import Settings
from rocket import Rocket

def run_rocket():

    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption("Roket fly")

    rocket = Rocket(ai_setting, screen)
    while True:
        rf.check_events(rocket)
        rocket.update()

        rf.update_screen(ai_setting, screen, rocket)


run_rocket()