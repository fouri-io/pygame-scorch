import pygame
from settings import FLOOR, PLAYER_MOVE_AMOUNT, SCREEN_WIDTH

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((60, 45))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(topleft=(10, FLOOR))
        # player_1 = pygame.image.load('graphics/character.png')

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.move_up()
        if keys[pygame.K_s]:
            self.move_down()
        if keys[pygame.K_a]:
            self.move_left()
        if keys[pygame.K_d]:
            self.move_right()

    def move_up(self):
        #print(self.rect.y)
        if self.rect.y <= 0:
            self.rect.y = 0
        else:
            self.rect.y -= PLAYER_MOVE_AMOUNT

    def move_down(self):
        if self.rect.y >= FLOOR:
            self.rect.y = FLOOR
        else:
            self.rect.y += PLAYER_MOVE_AMOUNT

    def move_left(self):
        if self.rect.left >= 0:
            self.rect.x -= PLAYER_MOVE_AMOUNT
        else:
            self.rect.left = 0

    def move_right(self):
        if self.rect.right <= SCREEN_WIDTH:
            self.rect.x += PLAYER_MOVE_AMOUNT
        else:
            self.rect.right = SCREEN_WIDTH

    def update(self):
        self.player_input()

    def fire(self, angle, speed):
        from projectile import Projectile  # Import here to avoid circular imports
        new_projectile = Projectile(self.rect.centerx, self.rect.top, angle, speed)
        return new_projectile