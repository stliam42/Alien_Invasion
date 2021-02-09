import pygame

class Ship():
    """ Class for ship managment"""

    def __init__(self, ai_game):
        """ Initialize the ship and start position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Download a ship image and get rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Every new ship spawn at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        def blitme(self):
            """ Paint the ship in the current position"""
            self.screen.blit(self.image, self.rect)
