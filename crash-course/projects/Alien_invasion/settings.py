class Settings:

    def __init__(self, width, height):

#       Ship
        self.screen_width = width
        self.screen_height = height
        self.bg_color = (0, 0, 0)
        self.ship_speed_factor = 1.5

#       Bullet
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 255, 255
        self.bullets_allowed = 3