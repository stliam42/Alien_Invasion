class Settings():
    """ Class for AI settings"""

    def __init__(self, *args, **kwargs):
        """ Initialize a game settings"""
        # Screen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship
        self.ship_speed = 1.5

        # Bullet
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (120, 60, 60)
        self.bullet_allowed = 3