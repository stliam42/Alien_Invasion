import pygame

class Alien(pygame.sprite.Sprite):
    """ Alien's class """
    def __init__(self, ai_game):
        """ Initialize an alien and set position """
        super().__init__()
        self.screen = ia_game.screen

        # Load an alien's image and get rect
        self.image = pygame.transform.rotate(pygame.image.load('images/x-wing.bmp'), 180)
        self.rect = self.image.get_rect()

        # Every new alien spawn in the top left corner
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Save real horisontal position
        self.x = float(self.rect.x)
