import pygame


class Tank:
    """A class for the tank"""

    def __init__(self, ai_game):
        """Initializes the tank"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        self.image = pygame.image.load('images/tank.bmp')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        """Pastes the tank image onto the screen"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Updates the tank's image coordinate"""
        if self.moving_right:
            self.x += self.settings.tank_speed
        if self.moving_left:
            self.x -= self.settings.tank_speed
        if self.moving_up:
            self.y -= self.settings.tank_speed
        if self.moving_down:
            self.y += self.settings.tank_speed

        self.rect.x = self.x
        self.rect.y = self.y

