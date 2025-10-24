import pygame

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720

images = {
    "basiccat": [pygame.image.load(f"assets/basic-cat/{i}.webp") for i in range(1, 4)],
    "tankcat": [pygame.image.load(f"assets/tank-cat/{i}.webp") for i in range(1, 4)],
    "doge": [pygame.image.load(f"assets/doge/{i}.webp") for i in range(1, 4)],
    "snache": [pygame.image.load(f"assets/snache/{i}.webp") for i in range(1, 4)],
}

spawn_point = (WINDOW_WIDTH - 150, WINDOW_HEIGHT - 200)
enemy_tower_pos = (200, WINDOW_HEIGHT - 200)

bg = pygame.transform.scale(
    pygame.image.load("assets/bg.png"), (WINDOW_WIDTH, WINDOW_HEIGHT)
)

cat_tower = pygame.image.load("assets/cat_tower.png")
cat_tower_rect = cat_tower.get_rect(bottomleft=(spawn_point[0] - 55, spawn_point[1]))

enemy_tower = pygame.image.load("assets/enemy_tower.png")
enemy_tower_rect = enemy_tower.get_rect(
    bottomright=(enemy_tower_pos[0] - 5, enemy_tower_pos[1])
)

cat_prices = {"basiccat": 50, "tankcat": 100}
