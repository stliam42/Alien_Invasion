class Settings():
    """ Class for AI settings"""

    def __init__(self, *args, **kwargs):
        """ Initialize a game settings"""
        # Screen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (10, 10, 10)

        # Ship
        self.ship_speed = 2
        self.ship_limit = 3

        # Bullet
        self.bullet_speed = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (250, 30, 30)
        self.bullet_allowed = 3

        # Aliens
        self.alien_speed = 1.0
        self.fleet_drop_speed = 150.0
        self.fleet_direction = 1 # 1 - moving right, -1 - moving left