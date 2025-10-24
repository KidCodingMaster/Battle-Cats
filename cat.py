import pygame
import random
from animation import Animation
from settings import *
import time


class Cat(pygame.sprite.Sprite):
    def __init__(self, health, attack, dps, cost, recharge, animation, speed):
        super().__init__()

        self.health = health  # Health of the cat
        self.attack = attack  # Attack strength of the cat
        self.dps = dps  # Delay before attacking
        self.cost = cost  # Cost of the cat
        self.recharge = recharge  # How long to recharge to buy
        self.speed = speed  # Speed the cat goes in

        self.animation = animation

        self.pos = pygame.Vector2(spawn_point)

        self.image = self.animation.img
        self.rect = self.image.get_rect(center=self.pos)

        self.window = pygame.display.get_surface()

        self.end_time = time.time()

        self.enemy_tower_health = 100

    def is_touching_tower(self):
        return self.pos.x <= enemy_tower_pos[0]
    
    def attack_(self):
        if time.time() >= self.end_time:
            self.end_time = time.time() + self.dps
            return True
        
        return False

    def update(self):
        if not self.is_touching_tower():
            self.pos.x -= self.speed

        self.animation.next_frame()

        self.image = self.animation.img
        self.rect.center = self.pos


class BasicCat(Cat, pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(
            health=100,
            attack=8,
            dps=1.23,
            cost=50,
            recharge=random.randint(2, 5),
            animation=Animation(images["basiccat"], speed=0.2),
            speed=2,
        )
