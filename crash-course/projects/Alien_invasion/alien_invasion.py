import pygame
import game_functions as gf

from pygame.sprite import Group
from settings import Settings
from ship import Ship


def run_game(width, height):
    pygame.init()
    ai_settings = Settings(width, height)
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                     ai_settings.screen_height))
    pygame.display.set_caption('Alien invasion')

    ship = Ship(screen, ai_settings)

    bullets = Group()


    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)


height, width = 700, 1050
run_game(width, height)
