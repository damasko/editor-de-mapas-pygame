import pygame


class Enemigo(pygame.sprite.Sprite):

    def __init__(self):
        super(Enemigo, self).__init__()
        self.nombre = "default_enemigo"
        self.vida = 0
        self.ataque = 0
        self.capa = 1
        self.surface = pygame.surface.Surface((64, 64)).convert()
        self.rect = self.surface.get_rect()

    def get_nombre(self):
        return self.nombre

