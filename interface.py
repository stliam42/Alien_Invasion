import pygame.font
from timer import Timer

class Button():
    """Button class"""

    def __init__(self, interface, msg,):
        """Initialize button's attributes"""
        self.screen = interface.screen
        self.screen_rect = interface.screen_rect

        # Assignment, size and properties
        self.width, self.height = 200, 50
        self.button_color = (0, 100, 180)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Creating button and centering it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Transform msg into rectangle and center it"""
        self.msg_image = self.font.render(msg, True, 
            self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
 
        
class Field():
    """Info field class"""

    def __init__(self, interface):
        """Initialize field's attributes"""
        self.screen = interface.screen
        # Assignment, size and properties
        self.bg_color = interface.settings.bg_color
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 30)
 

    def _prep_msg(self):
        """Transform msg into rectangle"""
        self.msg_image_rect = self.msg_image.get_rect()

    def draw(self):
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def update_text(self, msg):
        self.msg_image = self.font.render(msg, True, 
            self.text_color, self.bg_color)
        self._prep_msg()


class Interface():
    """Alien Invasion interface class"""

    def __init__(self, ai_game):
        """Initialize interface's attributes"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        self.timer = Timer()

        # Buttons
        self.play_button = Button(self, "Play")

        # Fields -------
        # Score
        self.score_field = Field(self)
        self.update_score()

        # Best score
        self.best_score_field = Field(self)
        self.update_best_score()

        # Time
        self.time_field = Field(self)
        self.update_time_field()

    def update_score(self):
        rounded_score = round(self.stats.score, -1)
        score_str = f"Score: {'{:,}'.format(rounded_score)}"
        self.score_field.update_text(score_str)
        self.score_field.msg_image_rect.right = self.screen_rect.right - 20
        self.score_field.msg_image_rect.top = 10

    def update_best_score(self):
        rounded_best_score = round(self.stats.best_score, -1)
        best_score_str = f"Best score: {'{:,}'.format(rounded_best_score)}"
        self.best_score_field.update_text(best_score_str)
        self.best_score_field.msg_image_rect.right = self.screen_rect.right - 20
        self.best_score_field.msg_image_rect.top = self.score_field.msg_image_rect.bottom + 10

    def update_time_field(self):
        self.time_field.update_text(self._format_time())
        self.time_field.msg_image_rect.midtop = self.screen.get_rect().midtop
        self.time_field.msg_image_rect.top = 10


    def update_interface(self):
        self.best_score_field.draw()
        self.score_field.draw()
        self.time_field.draw()
        self.timer.update_time()

    def _format_time(self):
        seconds = self.timer.time // 1000 
        minutes = seconds // 60
        seconds -= minutes * 60 
        return "{0:02}:{1:02}".format(minutes, seconds)




