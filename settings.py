class Settings():
    """ Class for AI settings"""

    def __init__(self, *args, **kwargs):
        """ Initialize a game settings"""
        # Screen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (10, 10, 10)

        # Ship
        self.ship_limit = 3

        # Bullet
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (250, 30, 30)
        self.bullet_allowed = 4

        # Aliens
        self.fleet_drop_speed = 150.0

        # Game temp
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize dynamic settings"""
        self.ship_speed = 2
        self.alien_speed = 1.0
        self.bullet_speed = 3.0
        self.alien_score = 50

        # Fleet direction
        self.fleet_direction = 1 # 1 - moving right, -1 - moving left

    def increase_speed(self):
        """Increase temp of the game"""
        self.ship_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_score = int(self.score_scale * self.alien_score)
            