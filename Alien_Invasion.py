import sys

import pygame

class AlienInvasion:
    """ Class for resourses managment and game behavior"""

    def __init__(self):
        """ Initialize the game and create game's resourses"""
        pygame.init()

        # Color
        self.bg_color = (230, 230, 230)

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion!")

    def run_game(self):
        """ Run the game cycle"""
        while True:
            # Tracking the keyboard and mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # Change screen
            self.screen.fill(self.bg_color)
            # Display the last screen
            pygame.display.flip()

if __name__ == '__main__':
    # Create the instance and start the game
    ai = AlienInvasion()
    ai.run_game()
