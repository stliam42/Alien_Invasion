import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion():
    """ Class for resourses managment and game behavior. """

    def __init__(self):
        """ Initialize the game and create game's resourses. """
        pygame.init()
        self.settings = Settings()

        # Color
        self.bg_color = (230, 230, 230)

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        #self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        #self.settings.screen_height = self.screen.get_rect().height
        #self.settings.screen_width = self.screen.get_rect().width
        pygame.display.set_caption("Alien Invasion!")

        self.ship = Ship(self)

    def run_game(self):
        """ Run the game cycle """
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            

    def _check_events(self):
        """ Tracking the keyboard and mouse """
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)

    def _update_screen(self):
        """ Change and display screen """
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        # Exit by 'Q'
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

if __name__ == '__main__':
    # Create the instance and start the game
    ai = AlienInvasion()
    ai.run_game()
