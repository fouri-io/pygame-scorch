import pygame
import time
from sys import exit
from player import Player
from target import Target
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FLOOR

def draw_text(surf, text, size, x, y, color):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topright = (x, y)
    surf.blit(text_surface, text_rect)

def initialize_targets():
    target1 = Target(430, FLOOR-20, 'graphics/enemy_fuel_canister.png')
    targets.add(target1)

    target2= Target(550, 370, 'graphics/enemy_fuel_canister.png')
    targets.add(target2)

    target3 = Target(850, 320, 'graphics/enemy_bomb.png')
    targets.add(target3)

    target5 = Target(1100, FLOOR -170, 'graphics/enemy_fuel_canister.png')
    targets.add(target5)

    target4 = Target(915, FLOOR - 35, 'graphics/enemy_tank_still.png')
    targets.add(target4)

# Initialize Game
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Scorch')
clock = pygame.time.Clock()
pygame.mixer.init()



# Initialize last update times
last_angle_update = time.time()
last_speed_update = time.time()

angle_update_interval = 0.1  # Seconds between updates
speed_update_interval = 0.1

# Prepare the background
background_surf = pygame.image.load('graphics/background_2.webp').convert()
background_surf = pygame.transform.scale(background_surf, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Play the music
pygame.mixer.music.load('music/Stoneworld Battle.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)
cannon_sound = pygame.mixer.Sound('music/cannon_fire_2.mp3')
cannon_sound.set_volume(0.9)

# Setup
all_sprites = pygame.sprite.Group()
projectiles = pygame.sprite.Group()
targets = pygame.sprite.Group()
initialize_targets()

current_angle = 45
current_speed = 20

player = Player()
all_sprites.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.start_firing_animation()
                cannon_sound.play()
                projectiles.add(player.fire(current_angle, current_speed))

    keys = pygame.key.get_pressed()

    current_time = time.time()  # Get the current time each frame

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and (current_time - last_angle_update > angle_update_interval):
        current_angle = max(0, current_angle - 1)
        last_angle_update = current_time  # Update the last modification time

    if keys[pygame.K_RIGHT] and (current_time - last_angle_update > angle_update_interval):
        current_angle = min(180, current_angle + 1)
        last_angle_update = current_time

    if keys[pygame.K_UP] and (current_time - last_speed_update > speed_update_interval):
        current_speed = min(50, current_speed + 1)
        last_speed_update = current_time

    if keys[pygame.K_DOWN] and (current_time - last_speed_update > speed_update_interval):
        current_speed = max(1, current_speed - 1)
        last_speed_update = current_time

    # Layer in background
    screen.blit(background_surf,(0,0))

    # Update all sprite groups
    all_sprites.update()
    projectiles.update()
    targets.update()

    # Collision detection
    hits = pygame.sprite.groupcollide(projectiles, targets, True, True)

    if hits:
        for projectile, hit_targets in hits.items():
            for target in hit_targets:
                print(f"Hit detected: Projectile at {projectile.rect.center} hit target at {target.rect.center}")

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
    for projectile in projectiles:
        screen.blit(projectile.surf, projectile.rect)
        if len(projectile.path) > 1:
            pygame.draw.lines(screen, (0, 255, 0), False, projectile.path, 2)  # Draw the path in green
    for target in targets:
        screen.blit(target.image, target.rect)

    # Display the current angle and speed
    draw_text(screen, f"Angle: {current_angle}°", 24, SCREEN_WIDTH - 10, SCREEN_HEIGHT - 50, (255, 255, 255))
    draw_text(screen, f"Speed: {current_speed}", 24, SCREEN_WIDTH - 10, SCREEN_HEIGHT - 20, (255, 255, 255))

    # Closing Loop
    pygame.display.update()
    clock.tick(60)
