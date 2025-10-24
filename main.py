import pygame
from settings import *
from cat import *
from enemy import *

pygame.init()


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        self.enemy_tower = 1000
        self.player_tower = 1000
        self.cats = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()

        self.clock = pygame.time.Clock()

        self.won = ""

        self.money = 0
        self.money_cap = 100
        self.money_increase = 2
        self.money_end_time = time.time() + 0.1

        self.font = pygame.font.SysFont("comicsans", 32)

        self.won_text = self.font.render("You won!", True, (255, 255, 255))
        self.lose_text = self.font.render("You lost!", True, (255, 255, 255))
        self.enemy_health_text = self.font.render(
            f"Health: {self.enemy_tower}", True, (0, 0, 0)
        )
        self.health_text = self.font.render(
            f"Health: {self.player_tower}", True, (0, 0, 0)
        )
        self.money_text = self.font.render(f"Money: {self.money}", True, (0, 0, 0))

        self.dog_end_time = time.time() + random.randint(5, 15)

    def run(self):
        while True:
            self.clock.tick(60)

            self.screen.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.money >= cat_prices["basiccat"]:
                            self.cats.add(BasicCat())
                            self.money -= cat_prices["basiccat"]
                    else:
                        if self.money >= cat_prices["tankcat"]:
                            self.cats.add(TankCat())
                            self.money -= cat_prices["tankcat"]

            if self.won == "":
                self.screen.blit(bg, (0, 0))

                if self.player_tower <= 0:
                    self.won = "yes"

                if self.enemy_tower <= 0:
                    self.won = "no"

                for cat in self.cats.sprites():
                    if cat.is_touching_tower():
                        if cat.attack_():
                            self.player_tower -= cat.attack

                for enemy in self.enemies.sprites():
                    if enemy.is_touching_tower():
                        if enemy.attack_():
                            self.enemy_tower -= enemy.attack

                if time.time() >= self.dog_end_time:
                    self.dog_end_time = time.time() + random.randint(5, 15)
                    self.enemies.add(random.choice([Doge(), Snache()]))

                if time.time() >= self.money_end_time:
                    self.money_end_time = time.time() + 0.1
                    if self.money+ 1 <= self.money_cap:
                        self.money += 1

                self.enemy_health_text = self.font.render(
                    f"Health: {self.enemy_tower}", True, (0, 0, 0)
                )
                self.health_text = self.font.render(
                    f"Health: {self.player_tower}", True, (0, 0, 0)
                )
                self.money_text = self.font.render(
                    f"Money: {self.money}", True, (0, 0, 0)
                )

                self.screen.blit(cat_tower, cat_tower_rect)
                self.screen.blit(enemy_tower, enemy_tower_rect)

                self.cats.draw(self.screen)
                self.cats.update(self.enemies)

                self.enemies.draw(self.screen)
                self.enemies.update(self.cats)

                self.screen.blit(
                    self.health_text,
                    (enemy_tower_pos[0] - 150, enemy_tower_pos[1] - 400),
                )
                self.screen.blit(
                    self.enemy_health_text,
                    (spawn_point[0] - 100, spawn_point[1] - 400),
                )
                self.screen.blit(
                    self.money_text,
                    (1000, 25),
                )
            elif self.won == "yes":
                self.screen.blit(self.won_text, (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
            elif self.won == "no":
                self.screen.blit(
                    self.lose_text, (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
                )
            else:
                exit()

            pygame.display.update()


if __name__ == "__main__":
    game = Game()

    game.run()
