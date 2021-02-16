import sys
import pygame
from time import sleep
from time import strftime

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from window import Window
from timer import Timer
from interface import Interface



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

        # Interface
        self.interface = Interface(self)

        # Windows
        self._create_windows()

    def _create_windows(self):
        """Creating score, ships, time windows"""

        # Ships
        self.ships_left_window = Window(self, f"Ships left: {self.stats.ships_left}")
        self.ships_left_window.msg_image_rect.left = self.screen.get_rect().left + 10
        self.ships_left_window.msg_image_rect.top = 10


    def run_game(self):
        """ Run the game cycle """
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._check_fleet_edges()
                self._update_aliens()
                self.interface.update_time_field()
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
            self.interface.play_button.draw()
        self.interface.update_interface()
        self._draw_window()
        pygame.display.flip()

    def _draw_window(self):
        self.ships_left_window.draw_window()

    def _update_score(self):
        rounded_score = round(self.stats.score, -1)
        score_str = '{:,}'.format(rounded_score)
        self.interface.score_field.update_text()
        self.interface.score_field.msg_image_rect.right = self.screen.get_rect().right - 20

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
        button_clicked = self.interface.play_button.rect.collidepoint(mouse_pos)
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

        # Reset timer
        self.interface.timer.reset_time()

        # Reset Score
        self.interface.update_score()

        # Reset settings
        self.settings.initialize_dynamic_settings()

    def _check_keydown_events(self, event):
        # Exit by 'Q'
        if event.key == pygame.K_q:
            sys.exit()
        if self.stats.game_active:
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = True
            elif event.key == pygame.K_SPACE:
                self._fire_bullet()
        else:
            # Start the game by 'P'
            if event.key == pygame.K_p:
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

        if collisions:
            for aliens in  collisions.values():
                self.stats.score += self.settings.alien_score * len(aliens)
            self.interface.update_score()
            self._check_best_score()   

        if not self.aliens:
            self.bullets.empty()
            self.settings.increase_speed()
            self._create_fleet()

        # Check collisions
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)

    def _check_best_score(self):
        if self.stats.score > self.stats.best_score:
            self.stats.best_score = self.stats.score
            self.interface.update_best_score()

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

            # Update ship's counter
            self.ships_left_window.update_text(f"Ships left: {self.stats.ships_left}")

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





