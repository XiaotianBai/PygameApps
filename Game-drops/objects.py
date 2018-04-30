import pygame, config, os
from random import randrange
from random import randint


class SquishSprite(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.display.init()
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        screen = pygame.display.set_mode(config.screen_size, 0)
        shrink_side = -config.margin_side * 2
        shrink_top = -config.margin_top * 2
        self.area = screen.get_rect().inflate(shrink_side, shrink_top)


class Weight(SquishSprite):

    def __init__(self, speed, index):
        SquishSprite.__init__(self, config.weight_image[index])
        self.speed = speed
        self.reset()
        self.landed = False

    def reset(self):
        x = randrange(self.area.left, self.area.right)
        self.rect.midbottom = x, 200

    def update(self):
        self.rect.top += self.speed
        self.landed = (self.rect.top >= self.area.bottom)


class Head(SquishSprite):
    def __init__(self):
        SquishSprite.__init__(self, config.head_image)
        self.rect.bottom = self.area.bottom
        self.pad_top = config.head_pad_top
        self.pad_side = config.head_pad_side

    def update(self):
        self.rect.centerx = pygame.mouse.get_pos()[0]
        self.rect = self.rect.clamp(self.area)

    def touches(self, other):
        bounds = self.rect.inflate(-self.pad_side, -self.pad_top)
        bounds.bottom = self.rect.bottom
        return bounds.colliderect(other.rect)


class Journalist(SquishSprite):

    def __init__(self, speed):
        SquishSprite.__init__(self, config.journalist_image)
        self.speed = speed
        self.reset()

    def reset(self):
        x = randrange(self.area.left, self.area.right)
        self.rect.midbottom = x, 250

    def update(self):
        self.rect.top += self.speed
        self.landed = self.rect.top >= self.area.bottom


class Wallace(SquishSprite):

    def __init__(self, speed):
        SquishSprite.__init__(self, config.wallace_image)
        self.speed = speed
        self.reset()

    def reset(self):
        x = randrange(self.area.left, self.area.right)
        self.rect.midbottom = x, 250

    def update(self):
        self.rect.top += self.speed
        self.landed = self.rect.top >= self.area.bottom


