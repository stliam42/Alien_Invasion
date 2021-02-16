import pygame
from random import choice

class Alien(pygame.sprite.Sprite):
    """ Alien's class """
    _aliens = ('alien_1.bmp',
               'alien_2.bmp',
               'alien_3.bmp')

    def __init__(self, ai_game):
        """ Initialize an alien and set position """
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load an alien's image and get rect
        self.image = pygame.transform.rotate(pygame.image.load('images/' + choice(self._aliens)), 180)
        self.rect = self.image.get_rect()

        # Every new alien spawn in the top left corner
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Save real horisontal position
        self.x = float(self.rect.x)

    def update(self):
        """ Update alien position """
        self.x += (self.settings.alien_speed *
                   self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """ Return True if an alien is at the edge of the screen """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True