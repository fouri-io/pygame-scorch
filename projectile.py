import pygame
import math
from settings import SCREEN_WIDTH, GRAVITY


class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, angle, speed):
        super().__init__()
        self.surf = pygame.Surface((10, 5))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(center=(x, y))
        self.speed = speed
        angle_rad = math.radians(angle)
        self.x_velocity = speed * math.cos(angle_rad)
        self.y_velocity = -speed * math.sin(angle_rad)  # Negative because y increases downwards
        self.path = []

    def update(self):
        # Update the position based on the velocity
        self.rect.x += self.x_velocity
        self.rect.y += self.y_velocity
        self.y_velocity += GRAVITY
        self.path.append((self.rect.centerx, self.rect.centery))

        # Remove the projectile if it passes the edge of the screen
        if self.rect.x > SCREEN_WIDTH or self.rect.y > 600:
            self.kill()
