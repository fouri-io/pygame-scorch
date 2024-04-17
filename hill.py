
# hill.py
import pygame

class Hill(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, image_path):
        super().__init__()
        self.image = pygame.Surface((width, height))  # Create a surface for the hill
        self.texture = pygame.image.load(image_path).convert_alpha()  # Load texture
        self.tile_texture(width, height)  # Tile the texture on the hill's surface
        self.rect = self.image.get_rect(midbottom=(x, y))

    def tile_texture(self, width, height):
        """Tile the texture across the surface of the hill."""
        for i in range(0, width, self.texture.get_width()):
            for j in range(0, height, self.texture.get_height()):
                self.image.blit(self.texture, (i, j))
