import pygame
from settings import FLOOR, PLAYER_MOVE_AMOUNT, SCREEN_WIDTH

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #self.surf = pygame.Surface((60, 45))
        #self.surf.fill((255, 255, 255))
        self.images = {
            'still': pygame.image.load('graphics/cannon_1_still.png').convert_alpha(),
            'mid': pygame.image.load('graphics/cannon_1_mid.png').convert_alpha(),
            'fire': pygame.image.load('graphics/cannon_1_fire.png').convert_alpha(),
        }
        self.current_image = 'still'
        self.animating = False
        self.animation_frames = ['still', 'mid', 'fire', 'mid', 'still']  # Order of animation
        self.current_frame = 0
        self.animation_speed = 9  # How fast to go through the animation cycle
        self.animation_counter = 0
        self.image = self.images[self.current_image]
        self.rect = self.image.get_rect(topleft=(60, 280))
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
        if self.animating:
            self.animation_counter += 1
            if self.animation_counter >= self.animation_speed:
                self.animation_counter = 0
                self.current_frame += 1
                if self.current_frame >= len(self.animation_frames):
                    self.current_frame = 0  # Reset to start
                    self.animating = False  # Stop animating after one cycle
                self.current_image = self.animation_frames[self.current_frame]
        self.image = self.images[self.current_image]
    def start_firing_animation(self):
        self.animating = True
        self.current_frame = 0
        self.animation_counter = 0

    def fire(self, angle, speed):
        from projectile import Projectile  # Import here to avoid circular imports
        new_projectile = Projectile(self.rect.right - 40, self.rect.centery - 35, angle, speed)
        return new_projectile