import os
import sys
import pygame
from pygame.locals import *
import random


class Card(pygame.sprite.Sprite):
    def __init__(self, number):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((80, 80))
        self.image.fill((0, 0, 0))
        pygame.draw.rect(self.image, (0, 0, 255), (5, 5, 70, 70))
        self.rect = self.image.get_rect()
        self.state = 0
        self.number = number
        self.flag = 0

    def click_on(self, number):
        if self.state == 0:
            if number == 0:
                my_font = pygame.font.SysFont('Comic Sans MS', 60)
                text = my_font.render('%s' % self.number, False, (255, 255, 255))
                self.image.blit(text, (5, 5))
                self.flag = self.number
                self.state = 1
            elif number == self.number:
                my_font = pygame.font.SysFont('Comic Sans MS', 60)
                text = my_font.render('%s' % self.number, False, (255, 255, 255))
                self.image.blit(text, (5, 5))
                self.flag = 0
                self.state = 1
            elif number != self.number:
                my_font = pygame.font.SysFont('Comic Sans MS', 60)
                text = my_font.render('%s' % self.number, False, (255, 0, 0))
                self.image.blit(text, (5, 5))
                self.flag = 10
                self.state = 1
            else: pass
        elif self.state == 1:
            pass

    def reset(self):
        self.image.fill((0, 0, 0))
        pygame.draw.rect(self.image, (0, 0, 255), (5, 5, 70, 70))
        self.state = 0
        self.flag = 0


class Game():
    def __init__(self):
        pygame.init()
        self.s = 0
        self.over = 0
        self.list = [i for i in range(1, 9)]
        self.list = self.list + self.list
        self.current_number = 0
        random.shuffle(self.list)
        pygame.display.set_caption("Guess")
        pygame.mouse.set_visible(True)

    def run(self):
        pygame.init()
        clock = pygame.time.Clock()
        screen_size = (1000, 800)
        screen = pygame.display.set_mode(screen_size, 0, 32)
        background = pygame.Surface(screen.get_size())
        background.fill((255, 255, 255))
        screen.blit(background, (0, 0))
        card_0 = Card(self.list[0])
        card_1 = Card(self.list[1])
        card_2 = Card(self.list[2])
        card_3 = Card(self.list[3])
        card_4 = Card(self.list[4])
        card_5 = Card(self.list[5])
        card_6 = Card(self.list[6])
        card_7 = Card(self.list[7])
        card_8 = Card(self.list[8])
        card_9 = Card(self.list[9])
        card_10 = Card(self.list[10])
        card_11 = Card(self.list[11])
        card_12 = Card(self.list[12])
        card_13 = Card(self.list[13])
        card_14 = Card(self.list[14])
        card_15 = Card(self.list[15])
        card_0.rect.center = (40, 40)
        card_1.rect.center = (120, 40)
        card_2.rect.center = (200, 40)
        card_3.rect.center = (280, 40)
        card_4.rect.center = (40, 120)
        card_5.rect.center = (120, 120)
        card_6.rect.center = (200, 120)
        card_7.rect.center = (280, 120)
        card_8.rect.center = (40, 200)
        card_9.rect.center = (120, 200)
        card_10.rect.center = (200, 200)
        card_11.rect.center = (280, 200)
        card_12.rect.center = (40, 280)
        card_13.rect.center = (120, 280)
        card_14.rect.center = (200, 280)
        card_15.rect.center = (280, 280)
        allSprites = pygame.sprite.Group(card_0, card_1, card_2, card_3, card_4, card_5, card_6, card_7, card_8,\
                                         card_9, card_10, card_11, card_12, card_13, card_14, card_15)
        keepGoing = True
        while keepGoing:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN:
                    x, y = event.pos
                    for card in allSprites:
                        if card.rect.collidepoint(x, y):
                            card.click_on(self.current_number)
                            allSprites.draw(screen)
                            pygame.display.flip()
                            self.current_number = card.flag
                            if self.current_number == 10:
                                pygame.time.delay(1000)
                                for cards in allSprites:
                                    cards.reset()
                                self.current_number = 0

        #    allSprites.update()
            allSprites.draw(screen)
            pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    game.run()
