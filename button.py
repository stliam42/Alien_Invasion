import pygame.font


class Button():
    """Button class"""

    def __init__(self, ai_game, msg, *position):
        """Initialize button's attributes"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Assignment, size and properties
        self.width, self.height = 200, 50
        self.button_color = (0, 100, 180)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Creating button and centering it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        if not position:
            self.rect.center = self.screen_rect.center
        else:
            self.rect.x, self.rect.y = position

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Transform msg into rectangle and center it"""
        self.msg_image = self.font.render(msg, True, 
            self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        
        

