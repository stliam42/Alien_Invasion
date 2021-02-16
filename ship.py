import pygame

class Ship(pygame.sprite.Sprite):
    """ Class for ship managment"""

    def __init__(self, ai_game):
        """ Initialize the ship and start position"""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Download a ship image and get rectangle
        self.image = pygame.image.load('images/x_wing.bmp')
        self.rect = self.image.get_rect()

        # Every new ship spawn at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.y -= 10

        #Moving flags
        self.moving_right = False
        self.moving_left = False

        # Save real coordinate ship's center
        self.x = float(self.rect.x)

    def blitme(self):
        """ Paint the ship in the current position"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """ Update ship's position """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update 'rect'
        self.rect.x = self.x

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.bottom = self.screen_rect.bottom - 10
        self.x = float(self.rect.x)