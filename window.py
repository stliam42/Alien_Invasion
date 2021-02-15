import pygame.font


class Window():
    """Window info class"""

    def __init__(self, ai_game, msg, side, *position):
        """Initialize button's attributes"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Assignment, size and properties
        self.width, self.height = 10, 10
        self.button_color = (0, 100, 180)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 30)

        # Creating button and centering it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        if not position:
            self.rect.center = self.screen_rect.center
        else:
            if side:
                self.rect.right, self.rect.top = position
            else:
            self.rect.left, self.rect.top = position

        self.update_text(msg)
        self._prep_msg()

    def _prep_msg(self):
        """Transform msg into rectangle and center it"""
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.topleft = self.rect.topleft

    def draw_window(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def update_text(self, text):
        self.msg_image = self.font.render(text, True, 
            self.text_color, self.button_color)
        




