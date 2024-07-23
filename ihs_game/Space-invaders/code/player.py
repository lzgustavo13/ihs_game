import pygame
from laser import Laser

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, screen_width, speed):
        super().__init__()
        self.image = pygame.image.load('../graphics/player.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=pos)
        self.speed = speed
        self.screen_width = screen_width
        self.ready = True
        self.laser_time = 0
        self.laser_cooldown = 600
        self.lasers = pygame.sprite.Group()

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.move_right()
        elif keys[pygame.K_LEFT]:
            self.move_left()
        if keys[pygame.K_SPACE] and self.ready:
            self.shoot()
            self.ready = False
            self.laser_time = pygame.time.get_ticks()

    def recharge(self):
        if not self.ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_time >= self.laser_cooldown:
                self.ready = True

    def constraint(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.screen_width:
            self.rect.right = self.screen_width

    def move_left(self):
        self.rect.x += self.speed
        self.constraint()

    def move_right(self):
        self.rect.x -= self.speed
        self.constraint()

    def shoot(self):
        if self.ready:
            laser = Laser(self.rect.center, -8, self.rect.bottom)
            self.lasers.add(laser)
            self.ready = False
            self.laser_time = pygame.time.get_ticks()

    def update(self):
        self.get_input()
        self.recharge()
        self.lasers.update()
