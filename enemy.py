import pygame
from animation import Animation
from settings import *
import time


class Enemy(pygame.sprite.Sprite):
    def __init__(self, health, attack, dps, speed, animation):
        super().__init__()

        self.health = health
        self.attack = attack
        self.dps = dps
        self.speed = speed

        self.animation = animation

        self.pos = pygame.Vector2(enemy_tower_pos)

        self.end_time = time.time()

        self.image = self.animation.img
        self.rect = self.image.get_rect(center=self.pos)

    def is_touching_tower(self):
        return self.pos.x >= spawn_point[0]

    def attack_(self):
        if time.time() >= self.end_time:
            self.end_time = time.time() + self.dps
            return True

        return False

    def update(self, cats):
        collided = []

        for cat in cats:
            if pygame.sprite.collide_mask(cat, self) is not None:
                collided.append(cat)

        if self.attack_():
            for cat in collided:
                cat.health -= self.attack

        if not self.is_touching_tower() and len(collided) <= 0:
            self.pos.x += self.speed

        if self.health <= 0:
            self.kill()

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


class Snache(Enemy):
    def __init__(self):
        super().__init__(
            health=100,
            attack=15,
            dps=1.23,
            speed=2,
            animation=Animation(images["snache"], speed=0.2),
        )
