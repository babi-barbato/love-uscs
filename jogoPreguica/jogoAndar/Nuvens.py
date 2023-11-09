from typing import Any
import pygame
import random
from pygame.locals import *

pygame.init()

LARGURA = 854 
ALTURA = 480

class Nuvem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./img/nuvem.png')
        self.image = pygame.transform.scale(self.image, (128*1.3, 62*3.3))
        self.rect = self.image.get_rect()
        self.rect.y = random.randrange(30, 100, 30)
        self.rect.x = LARGURA - random.randrange(30, 300, 90)

        self.velocidade = 3

    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = LARGURA
            self.rect.y = random.randrange(30, 100, 30)

        self.rect.x -= self.velocidade