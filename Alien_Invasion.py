import sys
import pygame
from time import sleep

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from window import Window


class AlienInvasion():
    """ Class for resourses managment and game behavior. """

    def __init__(self):
        """ Initialize the game and create game's resourses. """
        pygame.init()
        self.settings = Settings()

        # Screen
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        #self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        #self.settings.screen_height = self.screen.get_rect().height
        #self.settings.screen_width = self.screen.get_rect().width
        pygame.display.set_caption("Alien Invasion!")

        # Ship, aliens, bullets
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        # Statistic
        self.stats = GameStats(self)

        # Creating 'Play' button
        self.play_button = Button(self, "Play")
        self.score_window = Window(self, None, 10, 10)
        self.score_window.button_color = self.settings.bg_color


    def run_game(self):
        """ Run the game cycle """
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._check_fleet_edges()
                self._update_aliens()
            self._update_screen()
            

    def _update_screen(self):
        """ Change and display screen """
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)

        # 'Play' button is displayed when game isn't active
        if not self.stats.game_active:
            self.play_button.draw_button()
        self.score_window.draw_window()
        self.score_window.update_text(f"Ships left: {self.stats.ships_left}")
        pygame.display.flip()


    def _check_events(self):
        """ Tracking the keyboard and mouse """
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self._start_game()

    def _start_game(self):
        # Reset statictic
        self.stats.reset_stats()
        # Start the game
        self.stats.game_active = True

        # Conceal the mouse
        pygame.mouse.set_visible(False)

        # Clearing aliens and bullets
        self.aliens.empty()
        self.bullets.empty()

        # Creating new fleet
        self._create_fleet()
        self.ship.center_ship()

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        # Exit by 'Q'
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        # Start the game by 'P'
        elif event.key == pygame.K_p or event.key == pygame.K_SPACE:
            self._start_game()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """ Create new bullet and add it in group bullets """
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """ Update bullets' positions and delete old ones """
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)
        self._check_bullet_aliens_collisions()

    def _check_bullet_aliens_collisions(self):
        """Check collisions"""
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

        # Check collisions
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)

    def _create_fleet(self):
        """ Create an alien fleet """
        for row_number in range(self._get_number_rows()):
            for alien_number in range(self._get_number_aliens_in_a_row()):
                self._create_alien(alien_number, row_number)
        
    def _create_alien(self, alien_number, row_number):
        """ Create an alien """
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _get_number_aliens_in_a_row(self):
        """ Calculating the number of aliens in a row """
        alien = Alien(self)
        alien_width = alien.rect.width
        avaliable_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = avaliable_space_x // (2 * alien_width)
        return number_aliens_x

    def _get_number_rows(self):
        """ Calculating the number of row """
        alien = Alien(self)
        alien_height = alien.rect.height
        ship_height = self.ship.rect.height
        avaliable_space_y = (self.settings.screen_height - 
                             (4 * alien_height) - ship_height)
        number_rows = avaliable_space_y // (2 * alien_height)
        return number_rows

    def _update_aliens(self):
        self.aliens.update()

        # Check the collision "alien - ship"
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        #Checks if the aliens have made it to the bottom of the screen.
        self._check_aliens_bottom()

    def _check_fleet_edges(self):
        """ Check the fleet has reached 
            the edge of the screen """
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """ Drop the fleet and change the direction """
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        """Handles a ship collision with an alien."""
        if self.stats.ships_left > 1:
            #Decrease ships_left
            self.stats.ships_left -= 1

            #Deleting aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            #Creating new fleet and placing the ship in the center
            self._create_fleet()
            self.ship.center_ship()

            sleep(1)
        else:
            self.stats.ships_left = 0
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

       
    def _check_aliens_bottom(self):
        """Checks if the aliens have made it to the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break
