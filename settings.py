class Settings():
    """ Class for AI settings"""

    def __init__(self, *args, **kwargs):
        """ Initialize a game settings"""
        # Screen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (10, 10, 10)

        # Ship
        self.ship_speed = 1.5

        # Bullet
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (250, 30, 30)
        self.bullet_allowed = 3