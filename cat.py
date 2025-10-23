import pygame
import random
from animation import Animation
from settings import *


class Cat(pygame.sprite.Sprite):
    def __init__(self, health, attack, dps, cost, recharge, animation, speed, pos):
        super().__init__()

        self.health = health  # Health of the cat
        self.attack = attack  # Attack strength of the cat
        self.dps = dps  # Delay before attacking
        self.cost = cost  # Cost of the cat
        self.recharge = recharge  # How long to recharge to buy
        self.speed = speed  # Speed the cat goes in

        self.animation = animation

        self.pos = pygame.Vector2(pos)

        self.image = self.animation.img
        self.rect = self.image.get_rect(center=self.pos)

        self.window = pygame.display.get_surface()

    def update(self):
        self.pos.x -= self.speed

        if self.pos.x <= enemy_tower_pos[0]:
            self.kill()

        self.animation.next_frame()

        self.image = self.animation.img
        self.rect.center = self.pos


class BasicCat(Cat, pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__(
            health=100,
            attack=8,
            dps=6.49,
            cost=50,
            recharge=random.randint(2, 5),
            animation=Animation(basic_cat["run"], speed=0.2),
            speed=2,
            pos=pos,
        )
