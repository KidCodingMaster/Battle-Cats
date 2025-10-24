import pygame
from animation import Animation
from settings import *


class Enemy(pygame.sprite.Sprite):
    def __init__(self, health, attack, dps, speed, animation):
        super().__init__()

        self.health = health
        self.attack = attack
        self.dps = dps
        self.speed = speed

        self.animation = animation

        self.pos = pygame.Vector2(enemy_tower_pos)

        self.image = self.animation.img
        self.rect = self.image.get_rect(center=self.pos)

    def is_touching_tower(self):
        return self.pos.x >= spawn_point[0]

    def update(self):
        if not self.is_touching_tower():
            self.pos.x += self.speed

        self.animation.next_frame()

        self.image = self.animation.img
        self.rect.center = self.pos


class Doge(Enemy):
    def __init__(self):
        super().__init__(
            health=90,
            attack=8,
            dps=1.57,
            speed=1,
            animation=Animation(images["doge"], speed=0.2),
        )
