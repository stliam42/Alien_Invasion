import pygame.font


class Window():
    """Window info class"""

    def __init__(self, ai_game, msg):
        """Initialize button's attributes"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Assignment, size and properties
        self.bg_color = ai_game.settings.bg_color
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 30)

        self.update_text(msg)
        self._prep_msg()

    def _prep_msg(self):
        """Transform msg into rectangle"""
        self.msg_image_rect = self.msg_image.get_rect()

    def draw_window(self):
        #self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def update_text(self, text):
        self.msg_image = self.font.render(text, True, 
            self.text_color, self.bg_color)
        




