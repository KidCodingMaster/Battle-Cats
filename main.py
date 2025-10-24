import pygame
from settings import *
from cat import *
from enemy import Doge

pygame.init()


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        self.tower = 1000
        self.cats = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()

        self.clock = pygame.time.Clock()

        self.won = False

        self.font = pygame.font.SysFont("comicsans", 32)
        self.won_text = self.font.render("You won!", True, (255, 255, 255))
        self.health_text = self.font.render(f"Health: {self.tower}", True, (0, 0, 0))

    def run(self):
        while True:
            self.clock.tick(60)

            self.screen.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.cats.add(BasicCat())
                    self.enemies.add(Doge())

            if not self.won:
                self.screen.blit(bg, (0, 0))

                if self.tower <= 0:
                    self.won = True

                for cat in self.cats.sprites():
                    if cat.is_touching_tower():
                        if cat.attack_():
                            self.tower -= cat.attack

                self.health_text = self.font.render(
                    f"Health: {self.tower}", True, (0, 0, 0)
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
            else:
                self.screen.blit(self.won_text, (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))

            pygame.display.update()


if __name__ == "__main__":
    game = Game()

    game.run()
