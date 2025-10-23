import pygame

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720

basic_cat = {
    "run": [pygame.image.load(f"assets/basic-cat/run/{i}.webp") for i in range(1, 4)]
}

spawn_point = (WINDOW_WIDTH - 100, WINDOW_HEIGHT - 150)
enemy_tower_pos = (100, WINDOW_HEIGHT - 100)
