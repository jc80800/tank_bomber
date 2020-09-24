import sys
import pygame
from settings import Settings
from tank import Tank


class TankGame:
    """Class for the Tank Game"""

    def __init__(self):
        """Initializes the game"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("A Tank Game")

        self.tank = Tank(self)

    def run_game(self):
        """Runs the game"""
        while True:
            self._check_event()
            self.tank.update()
            self._update_screen()

    def _check_event(self):
        """Checks for events (helper)"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.tank.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.tank.moving_left = True
                elif event.key == pygame.K_UP:
                    self.tank.moving_up = True
                elif event.key == pygame.K_DOWN:
                    self.tank.moving_down = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.tank.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.tank.moving_left = False
                elif event.key == pygame.K_UP:
                    self.tank.moving_up = False
                elif event.key == pygame.K_DOWN:
                    self.tank.moving_down = False

    def _update_screen(self):
        """Updates the screen (helper)"""
        self.screen.fill(self.settings.bg_color)
        self.tank.blitme()
        pygame.display.flip()


if __name__ == '__main__':
    ai = TankGame()
    ai.run_game()
