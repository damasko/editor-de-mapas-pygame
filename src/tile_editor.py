import pygame


class Tile(pygame.sprite.Sprite):
    # constructor :
    def __init__(self):
        super(Tile, self).__init__()
        self.nombre = "default"
        self.surface = pygame.surface.Surface((32, 32)).convert_alpha()
        #self.rect = self.surface.get_rect()
        self.x = 0
        self.y = 0
        self.tipo = "0"
        self.tipo_parent = "0"
        self.caminable = True
