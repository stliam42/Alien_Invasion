class GameStats():
    """Statistic for Alien Invasion"""

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        """Initialize statistics that will change during the game"""
        self.ships_left = self.settings.ship_limit
