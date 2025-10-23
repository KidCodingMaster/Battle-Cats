import pygame


class Animation:
    def __init__(self, imgs, flip_x=False, flip_y=False, scale=1, speed=0.4):
        # self.imgs = list(map(lambda x: pygame.image.load(x).convert_alpha(), imgs))
        self.imgs = imgs

        self.speed = speed

        if flip_x or flip_y:
            self.imgs = list(
                map(lambda x: pygame.transform.flip(x, flip_x, flip_y), self.imgs)
            )

        if scale != 1:
            self.imgs = list(
                map(
                    lambda x: pygame.transform.scale(
                        x, (x.get_width() * scale, x.get_height() * scale)
                    ),
                    self.imgs,
                )
            )

        self.img_count = 0
        self.img = self.imgs[self.img_count]

    def next_frame(self):
        if self.img_count + 1 < len(self.imgs):
            self.img_count += self.speed
        else:
            self.img_count = 0

        self.img = self.imgs[int(self.img_count)]

    def draw(self, win, coor):
        win.blit(self.img, coor)
