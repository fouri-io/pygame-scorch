import pygame


class Target(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.surf = pygame.Surface((width, height))
        self.surf.fill((0,128,255))
        self.rect = self.surf.get_rect(center=(x,y))
