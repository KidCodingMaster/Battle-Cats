import pygame


class Button:
    def __init__(self, text, width, height, x, y):
        self.size = (width, height)
        self.pos = (x, y)

        self.button_rect = pygame.Rect(*self.pos, *self.size)
        self.button_text = pygame.font.SysFont("cosmicsansms", 32).render(
            text, False, (255, 255, 255)
        )

    def draw(self, screen):
        pygame.draw.rect(
            screen,
            (255, 0, 0),
            self.button_rect,
        )
        screen.blit(
            self.button_text,
            (self.pos[0] + self.size[0] // 3, self.pos[1] + self.size[1] // 3),
        )

    def is_clicked(self):
        pos = pygame.mouse.get_pos()

        return pygame.mouse.get_pressed()[0] and self.button_rect.collidepoint(*pos)
