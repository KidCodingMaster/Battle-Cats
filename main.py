import pygame
from settings import *
from cat import *

pygame.init()


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        self.cat = BasicCat(spawn_point)

        self.all_sprites = pygame.sprite.Group(self.cat)

        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            self.clock.tick(60)

            self.screen.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break

            self.all_sprites.draw(self.screen)
            self.all_sprites.update()

            pygame.display.update()


if __name__ == "__main__":
    game = Game()

    game.run()
