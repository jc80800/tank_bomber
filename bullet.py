import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Class for bullet"""
    def __init__(self, ai_game):
        """Initializes a bullet object"""
        super().__init__()
        self.screen = ai_game.screen
        self.setting = ai_game.settings
        self.color = self.setting.bullet_color

        self.rect = pygame.Rect(0, 0, self.setting.bullet_width, self.setting.bullet_height)
        self.rect.midtop = ai_game.tank.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        """Updates bullet position by going up"""
        self.y -= self.setting.bullet_speed

        self.rect.y = self.y

    def draw_bullet(self):
        """Draws the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
