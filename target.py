import pygame


class Target(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path, width=None, height=None):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(center=(x,y))
