import sys
import pygame
from settings import Settings
from tank import Tank
from bullet import Bullet

class TankGame:
    """Class for the Tank Game"""

    def __init__(self):
        """Initializes the game"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("A Tank Game")

        self.tank = Tank(self)
        self.bullet = pygame.sprite.Group()

    def run_game(self):
        """Runs the game"""
        while True:
            self._check_event()
            self.tank.update()
            self._update_bullet()
            self._update_screen()

    def _check_event(self):
        """Checks for events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_events_keydown(event)
            elif event.type == pygame.KEYUP:
                self._check_events_keyup(event)

    def _check_events_keydown(self, event):
        """Checks for keydown events"""
        if event.key == pygame.K_RIGHT:
            self.tank.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.tank.moving_left = True
        elif event.key == pygame.K_UP:
            self.tank.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.tank.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_events_keyup(self, event):
        """Checks for keyup events"""
        if event.key == pygame.K_RIGHT:
            self.tank.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.tank.moving_left = False
        elif event.key == pygame.K_UP:
            self.tank.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.tank.moving_down = False

    def _fire_bullet(self):
        """Produces a new bullet object and adds it to the 'bullet' list"""
        new_bullet = Bullet(self)
        self.bullet.add(new_bullet)

    def _update_bullet(self):
        """Updates the bullet and removes bullets that reaches out of screen"""
        self.bullet.update()
        for bullet in self.bullet.copy():
            if bullet.rect.bottom < 0:
                self.bullet.remove(bullet)

    def _update_screen(self):
        """Updates the screen """
        self.screen.fill(self.settings.bg_color)
        self.tank.blitme()
        for bullet in self.bullet.sprites():
            bullet.draw_bullet()
        pygame.display.flip()


if __name__ == '__main__':
    ai = TankGame()
    ai.run_game()
