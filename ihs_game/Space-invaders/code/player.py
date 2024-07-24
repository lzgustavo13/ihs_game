import pygame 
from laser import Laser
from fcntl import ioctl
from integracao import *

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,constraint,speed):
        super().__init__()
        self.image = pygame.image.load('../graphics/player.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = pos)
        self.speed = speed
        self.max_x_constraint = constraint
        self.ready = True
        self.laser_time = 0
        self.laser_cooldown = 600

        self.lasers = pygame.sprite.Group()

        self.laser_sound = pygame.mixer.Sound('../audio/laser.wav')
        self.laser_sound.set_volume(0.5)
        
    def get_input(self):
        Integration=IO()
        if Integration.get_PB(0)==0:
            self.move_right()
        if Integration.get_PB(1)==0:
            self.move_left()
        if Integration.get_PB(3)==0 and self.ready:
            self.shoot()
            self.ready = False
            self.laser_time = pygame.time.get_ticks()
            self.laser_sound.play()

    def recharge(self):
        if not self.ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_time >= self.laser_cooldown:
                self.ready = True

    def constraint(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.max_x_constraint:
            self.rect.right = self.max_x_constraint
    def move_left(self):
            self.rect.x -= self.speed
            self.constraint()

    def move_right(self):
        self.rect.x += self.speed
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
