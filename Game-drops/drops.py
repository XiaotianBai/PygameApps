import os
import sys
import pygame
from pygame.locals import *
import objects
import config
import progressbar
import random


class State:

    def handle(self, event):
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            sys.exit()

    def firstDisplay(self, screen):
        screen.fill(config.background_color)
        pygame.display.flip()

    def display(self, screen):
        pass


class Level(State):

    def __init__(self, number=1):
        pygame.init()
        self.number = number
        self.remaining = config.weights_per_level
        self.progress = 50
        self.speed = config.drop_speed
        self.speed += (self.number-1) * config.speed_increase
        self.bar_font = pygame.font.SysFont('SimHei', 40)
        self.title = u'X.T.B.Progress.Bar'
        self.bar = progressbar.TextProgress(self.bar_font, self.title, (0, 0, 0), (255, 255, 255))
        self.random = random.randint(0, 3)
        self.weight = objects.Weight(config.speed[self.random]+self.number-1, self.random)
        self.head = objects.Head()
        both = self.weight, self.head
        self.sprites = pygame.sprite.RenderUpdates(both)

    def update(self, game):
        self.sprites.update()
        if self.head.touches(self.weight):
            self.progress += config.score[self.random]
            self.random = random.randint(0, 3)
            self.weight.__init__(config.speed[self.random]+self.number-1, self.random)
            if self.progress >= 100:
                game.nextState = LevelCleared(self.number)
            elif self.progress <= 0:
                game.nextState = GameOver()
        elif self.weight.landed:
            if self.random == 0 or self.random == 2:
                self.progress -= 10
                if self.progress <= 0:
                    game.nextState = GameOver()
            self.random = random.randint(0, 3)
            self.weight.__init__(config.speed[self.random]+self.number-1, self.random)


    def display(self, screen):
        screen.fill(config.background_color)
        updates = self.sprites.draw(screen)
        pygame.display.update(updates)
        text = self.bar.render(self.progress)
        screen.blit(text, (300, 20))
        pygame.display.flip()


class Paused(State):
    finished = 0

    def __init__(self):
        self. finished = 0
    image = None
    text = 'Paused '

    def handle(self, event):
        State.handle(self, event)
        if event.type in [MOUSEBUTTONDOWN, KEYDOWN]:
            self.finished = 1

    def update(self, game):
        if self.finished:
            self.finished = 0
            game.nextState = self.nextState

    def firstDisplay(self, screen):
        pygame.init()
        screen.fill(config.background_color)
        #font = pygame.font.Font(None, config.font_size)
        font = pygame.font.SysFont('SimHei', 40)
        lines = self.text.strip().splitlines()
        height = len(lines) * font.get_linesize()
        center, top = screen.get_rect().center
        top -= height // 2
        if self.image:
            image = pygame.image.load(self.image).convert()
            r = image.get_rect()
            top += r.height // 2
            r.midbottom = center, top - 20
            screen.blit(image, r)

        antialias = 1
        black = 0, 0, 0

        for line in lines:
            text = font.render(line.strip(), antialias, black)
            r = text.get_rect()
            r.midtop = center, top
            screen.blit(text, r)
            top += font.get_linesize()

        pygame.display.flip()


class Info(Paused):
    nextState = Level()
    text = 'Go!'


class StartUp(Paused):
    nextState = Info()
    image = config.welcome_image
    text = 'Survive as long as you can'


class LevelCleared(Paused):

    def __init__(self, number):
        self.number = number
        self.text = 'Level %s completed!' % self.number
        LevelCleared.nextState = Level(self.number+1)


class GameOver(Paused):

    def __init__(self):
        GameOver.nextState = Level()
        GameOver.text = 'You Lost!'


class Game():
    def __init__(self, *args):
        path = os.path.abspath(args[0])
        dir = os.path.split(path)[0]
        os.chdir(dir)
        self.state = None
        self.nextState = StartUp()

    def run(self):
        pygame.init()
        self.state = State()
        flag = 0
        if config.full_screen:
            flag = FULLSCREEN
        screen_size = config.screen_size
        screen = pygame.display.set_mode(screen_size, flag, 32)
        pygame.display.set_mode(screen_size, flag)
        pygame.display.set_caption('Xiaotian Bai')
        pygame.mouse.set_visible(False)
        while True:
            if self.state != self.nextState:
                self.state = self.nextState
                self.state.firstDisplay(screen)

            for event in pygame.event.get():
                self.state.handle(event)
            self.state.update(self)
            self.state.display(screen)

if __name__ == '__main__':
    new_game = Game(*sys.argv)
    new_game.run()





