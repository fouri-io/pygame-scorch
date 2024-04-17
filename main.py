import pygame
from sys import exit
from player import Player
from projectile import Projectile

pygame.init()
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Scorch')
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
projectiles = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                projectiles.add(player.fire())

    screen.fill("purple")
    all_sprites.update()
    projectiles.update()

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    for projectile in projectiles:
        screen.blit(projectile.surf, projectile.rect)
        if len(projectile.path) > 1:
            pygame.draw.lines(screen, (0, 255, 0), False, projectile.path, 2)  # Draw the path in green

    pygame.display.update()
    clock.tick(60)
